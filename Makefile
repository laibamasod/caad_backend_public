run:
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

install:
	pip3 install -r requirements.txt

run-gunicorn:
	python3 manage.py makemigrations
	python3 manage.py migrate
	gunicorn cms_backend_api.wsgi:application --bind 0.0.0.0:8000 --access-logfile /home/caad/access.log --error-logfile /home/caad/error.log


