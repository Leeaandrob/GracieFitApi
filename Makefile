clean:
	find . -name "*.pyc" -exec rm -rf {} \;

run: clean
	python manage.py runserver

migrations: clean
	python manage.py makemigrations

migrate: clean
	python manage.py migrate

superuser:
	python manage.py createsuperuser

shell:
	python manage.py shell