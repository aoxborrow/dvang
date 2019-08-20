default: run

run:
	django/manage.py runserver 0.0.0.0:80

load:
	django/manage.py makemigrations
	django/manage.py migrate
	django/manage.py loaddata django/fixtures/*

migrate:
	django/manage.py makemigrations
	django/manage.py migrate

collect:
	django/manage.py collectstatic --noinput

clean:
	find . -name "__pycache__" -print0 | xargs -0 rm -rf
	find . -name "*.pyc" -print0 | xargs -0 rm

start:
	sudo supervisorctl start gunicorn
	sudo service nginx start

restart:
	sudo supervisorctl restart gunicorn
	sudo service nginx restart

stop:
	sudo supervisorctl stop gunicorn
	sudo service nginx stop

install-galaxy-roles:
	sudo ansible-galaxy install --roles-path ansible/roles -r ansible/requirements.yml

provision-dev:
	sudo ansible-playbook -c local ansible/dev.yml

provision-prod:
	sudo ansible-playbook -c local ansible/prod.yml
