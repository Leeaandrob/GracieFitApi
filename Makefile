clean:
	find . -name "*.pyc" -exec rm -rf {} \;

run: clean
	python manage.py runserver