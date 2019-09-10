default: run

run:
	src/manage.py runserver 0.0.0.0:80

load:
	src/manage.py makemigrations
	src/manage.py migrate
	src/manage.py loaddata src/fixtures/*

migrate:
	src/manage.py makemigrations
	src/manage.py migrate

collect:
	src/manage.py collectstatic --noinput

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
	ansible-galaxy install --roles-path ansible/roles -r ansible/requirements.yml

provision-dev:
	ansible-playbook -c local ansible/dev.yml

provision-prod:
	ansible-playbook -c local ansible/prod.yml
