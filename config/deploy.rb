set :stages, %w(prod)
set :default_stage, "prod"
set :application, "graciefitapi"

require 'capistrano/ext/multistage'

set :user, 'webapps'
set :use_sudo, true

set :repository,  "git@github.com:Leeaandrob/graciefitapi.git"
set :ssh_options, {:forward_agent => true}
default_run_options[:pty] = true
set :sudo_prompt, "ufitteam123456"

set :branch, "master"
set :scm, :git


set :deploy_to, "/home/webapps/#{application}"
set :copy_dir, "/tmp"
set :copy_remote_dir, "/tmp"
set :copy_exclude, [".git", ".gitignore", "*.pyc", "**/.git", "**/*.log", "**/.pyc", ".swp", ".swp", "Gemfile", "tmp/", '**/.gitignore', 'Capfile', 'REVISION', 'Vagrant', 'Gemfile.lock', '**/Vagrant', '**/Capfile', '**/REVISION']


set :keep_releases, 3

after "deploy:restart", "deploy:cleanup"

namespace :deploy do
	task :upload_files do
		top.upload("config/deploy_config/graciefit.conf", "#{deploy_to}/graciefit.conf")
	end
	task :finalize_update do
		#nao quero que execute isso
	end
	desc "Atualizacao e instalacao de depedencias para o projeto"
	task :setup do
		run "echo Setup Server"

		run "mkdir -p /home/webapps/#{application}/ /home/webapps/#{application}/releases /home/webapps/#{application}/shared /home/webapps/#{application}/shared/system /home/webapps/#{application}/shared/log /home/webapps/#{application}/shared/pids"
		run "chmod g+w /home/webapps/#{application}/ /home/webapps/#{application}/releases /home/webapps/#{application}/shared /home/webapps/#{application}/shared/system /home/webapps/#{application}/shared/log /home/webapps/#{application}/shared/pids"
		run "ln -s -f #{deploy_to}/shared/log/ #{deploy_to}/logs"

		top.upload("config/deploy_config/ssh/id_rsa", "/home/webapps/.ssh/id_rsa")
		top.upload("config/deploy_config/ssh/id_rsa.pub", "/home/webapps/.ssh/id_rsa.pub")
		top.upload("config/deploy_config/graciefit.ini", "#{deploy_to}/graciefit.ini")
		top.upload("config/deploy_config/graciefit.conf", "#{deploy_to}/graciefit.conf")
		top.upload("config/deploy_config/graciefit_super.conf", "#{deploy_to}/graciefit_super.conf")

		run "echo GIT"
		run "chmod 0644 ~/.ssh/id_rsa && chmod 0644 ~/.ssh/id_rsa.pub"
		run "chmod 777 ~/.ssh/id_rsa && chmod 777 ~/.ssh/id_rsa.pub"
		run "chmod 400 ~/.ssh/id_rsa && chmod 400 ~/.ssh/id_rsa.pub"


		run "echo Atualizando"
		run "sudo -i add-apt-repository -y ppa:rwky/redis"
		run "sudo apt-get -y install python-dev python2.7-dev python-virtualenv postgresql postgresql-contrib libpq-dev nginx supervisor libreadline-dev libncurses5-dev libffi-dev git redis-server"

		run "echo Configurando"
		run "cd #{deploy_to} && virtualenv . "
		run "mv -f #{deploy_to}/graciefit.ini #{deploy_to}/shared/"
		run "touch #{deploy_to}/shared/log/out.log"
		run "touch #{deploy_to}/shared/log/err.log"
		run "touch #{deploy_to}/shared/log/celery-worker.log"
		run "sudo -i mv -f #{deploy_to}/graciefit.conf /etc/nginx/sites-enabled/"
		run "sudo -i ln -sf /etc/nginx/sites-enabled/graciefit.conf /etc/nginx/sites-available/graciefit.conf"
		run "sudo -i mv -f #{deploy_to}/graciefit_super.conf /etc/supervisor/conf.d/"
		run "sudo -i supervisorctl reread"
		run "sudo -i supervisorctl update"
		run "ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts"
		run "#{deploy_to}/run"
		run "#{deploy_to}/run/uwsgi.sock"
	end

	task :restart, :roles => :app do
		python_path = "#{deploy_to}/bin/python"
		run "echo baz"
		run "#{deploy_to}/bin/pip install -r #{deploy_to}/current/requirements_production.txt"
		run "#{python_path} #{deploy_to}/current/manage.py migrate --settings=graciefitapi.settings_production"
		run "rm #{deploy_to}/current/**/migrations/*[0-9]*.py && rm #{deploy_to}/current/**/migrations/*[0-9]*.pyc"
		run "#{python_path} #{deploy_to}/current/manage.py makemigrations --settings=graciefitapi.settings_production"
		run "sudo service nginx restart"
		run "sudo supervisorctl restart all"
		end
	end