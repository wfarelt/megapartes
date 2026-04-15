# megapartes
Pagina web para la empresa Megapartes

# pip freeze
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt

# iconos
https://codesinging.github.io/bootstrap-icons-font/#icons


chmod +x deploy.sh

# postgres

sudo -u postgres psql

ALTER ROLE wfarel SET client_encoding TO 'utf8';
ALTER ROLE wfarel SET default_transaction_isolation TO 'read committed';
ALTER ROLE wfarel SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE megapartes_prod TO wfarel;

\q

# Testing Gunicorn’s Ability to Serve the Project

gunicorn --bind 0.0.0.0:8000 myproject.wsgi

# Step 7 — Creating systemd Socket and Service Files for Gunicorn

sudo nano /etc/systemd/system/gunicorn.socket

sudo nano /etc/systemd/system/gunicorn.service

sudo systemctl daemon-reload
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket

sudo systemctl status gunicorn.socket
sudo systemctl status gunicorn


sudo nano /etc/nginx/sites-available/megapartes
sudo ln -s /etc/nginx/sites-available/megapartes /etc/nginx/sites-enabled

sudo systemctl restart nginx

# Step 10 — Configure Nginx to Proxy Pass to Gunicorn
sudo nano /etc/nginx/sites-available/megapartes
sudo ln -s /etc/nginx/sites-available/megapartes /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'


sudo systemctl restart gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn.socket gunicorn.service
sudo nginx -t && sudo systemctl restart nginx

python manage.py collectstatic --noinput
sudo chown -R www-data:www-data /home/wfarel/megapartes/static
sudo chmod -R 755 /home/wfarel/megapartes/static
sudo systemctl restart nginx
