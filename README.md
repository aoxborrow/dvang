DVANG
=======

### Django-Vagrant-Ansible-Nginx-Gunicorn *Starter Pack*

This is a starter pack for quickly developing a Django project locally with Vagrant, which is then easily deployed into production with Ansible. It installs and configures all the services you'll need:
 - Vagrant VM based on Ubuntu 18.04
 - Python 3.6 virtualenv for your Django app and its dependencies
 - Nginx to serve static files and proxy to Gunicorn
 - Supervisor to automatically start/restart Gunicorn
 - PostgreSQL with database and initial Django migrations
 - Minimal Django configuration with Django Admin and Debug Toolbar
 - Node.js for installing front-end components *(optional)*

### Features
- disposable environment is fully self-contained within the Vagrant VM
- Ansible playbooks for both local development and production
- develop with Django dev server, then test/deploy with Gunicorn/Nginx
- easily add Ansible galaxy roles *(ansible/requirements.yml)*
- activates Python virtualenv on login
- installs Python packages from `requirements.txt`
- installs Node packages from `package.json`
- configure environment-specific Django settings in `settings_local.py`

### Shortcuts
- run Django devserver `make run`
- makemigrations and migrate `make migrate`
- load Django fixtures `make load`
- Django collect static files `make collect`
- start or restart Gunicorn/Nginx: `make restart`
- activate the virtualenv `activate`
- deactivate the virtualenv `deactivate`
- run playbook for dev `make provision-dev` *(must deactivate virtualenv)*
- run playbook production `make provision-prod` *(must deactivate virtualenv)*
----

### Local Development

0. Install [Vagrant](https://www.vagrantup.com/)

0. Clone this repo as your project name: **(This is important, the project folder name will be used for configuring database name, hostname, etc.)**
    ```sh
    git clone git@github.com:paste/dvang.git my-project-name
    ```

0. Build your Vagrant VM:

    ```sh
    vagrant up
    ```

0. Log into the VM via SSH:
    ```sh
    vagrant ssh
    ```

0. Start Django development server:
    ```sh
    cd my-project-name
    make run
    ```

0. Modify your computer's local `/etc/hosts`:

    ```
    192.168.33.55   my-project-name.local
    ```

0. Visit your app:
    ```
    http://my-project-name.local
    ```

0. Login to Django Admin with user/pass: **admin/admin**:
    ```
    http://my-project-name.local/admin
    ```


0. **Profit** :heavy_check_mark:


----

### In Production

0. You'll need a hosting account with `sudo` privileges to run Ansible. If you only have a `root` user, create a new user and grant them `sudo` access: https://www.digitalocean.com/community/tutorials/how-to-create-a-sudo-user-on-ubuntu-quickstart

0. Edit the `host_name` and other settings in `ansible/prod.yml` as necessary.

0. Clone your project onto the server in your remote user's home folder, e.g. `~/my-project-name`

0. Install Ansible with the included script:
    ```sh
    cd ~/my-project-name
    sudo ansible/install.sh
    ```

0. Install Ansible Galaxy roles:
    ```sh
    make install-galaxy-roles
    ```

0. Run the Ansible production playbook:
    ```sh
    make provision-prod
    ```

0. Activate the virtualenv:
    ```sh
    activate
    ```

0. Apply Django migrations:
    ```sh
    make migrate
    ```

0. Load Django fixtures:
    ```sh
    make load
    ```

0. Collect Django static files:
    ```sh
    make collect
    ```

0. Restart Gunicorn:
    ```sh
    make restart
    ```

0. **Profit** :heavy_check_mark:


----

### HTTPS in Production

0. To use HTTPS you will need an SSL certificate. Get one from Certbot here: https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx

0. Copy the certificate and key to your remote user's home folder. The Nginx configuration expects the files to be named after the `host_name`, like this:  
    ```
    ~/dvang.io.crt
    ~/dvang.io.key
    ```

0. Update the production playboook to use SSL, in `ansible/prod.yml`:  
    ```yaml
    nginx_use_ssl: true
    ```

0. Enable SSL features for Django, in `django/settings_local.py`:  
    ```py
    # this enables secure cookies, HTTP redirect, etc.
    USE_SSL = True
    ```

0. Re-run the Ansible production playbook:
    ```sh
    make provision-prod
    ```

0. **Profit** :heavy_check_mark:
