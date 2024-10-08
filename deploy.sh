#!/bin/bash

# Declarar variables
usuario="wfarel"
password="wf12345*"
nombre_proyecto="megapartes"
entorno_virtual="venv"
server_ip="192.168.0.25"
$proyecto="mega"

# Actualizar el sistema y los paquetes
echo "Actualizando el sistema..."
sudo apt update && sudo apt upgrade -y

# Instalar dependencias
echo "Instalando dependencias..."
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl

# Cambiar al usuario postgres y configurar la base de datos y usuario
sudo -u postgres psql <<EOF
-- Crear base de datos
CREATE DATABASE ${nombre_proyecto}_prod;

-- Crear usuario con contraseña
CREATE USER $usuario WITH PASSWORD '$password';

-- Configurar codificación y transacción
ALTER ROLE $usuario SET client_encoding TO 'utf8';
ALTER ROLE $usuario SET default_transaction_isolation TO 'read committed';
ALTER ROLE $usuario SET timezone TO 'UTC';

-- Dar todos los privilegios al usuario sobre la base de datos
GRANT ALL PRIVILEGES ON DATABASE ${nombre_proyecto}_prod TO $usuario;

-- Salir de psql
\q
EOF

echo "PostgreSQL instalado y configurado con éxito."
echo "Base de datos: ${nombre_proyecto}_prod"
echo "Usuario: $usuario"

# Navegar al directorio del proyecto
cd /home/$usuario/$nombre_proyecto

# Activar el entorno virtual
echo "Activando entorno virtual..."
# Crear un entorno virtual
python3 -m venv $entorno_virtual
source /home/$usuario/$nombre_proyecto/$entorno_virtual/bin/activate

# Instalar dependencias del proyecto
echo "Instalando dependencias del proyecto $nombre_proyecto..."
pip install -r requirements.txt

# Configurar Gunicorn
echo "Configurando Gunicorn..."
pip install django gunicorn psycopg2-binary

# Migrar la base de datos
echo "Aplicando migraciones..."
python manage.py makemigrations
python manage.py migrate

# Recopilar archivos estáticos
echo "Recopilando archivos estáticos para $nombre_proyecto..."
python manage.py collectstatic --noinput

# Crear un superusuario
python manage.py createsuperuser

# Desactivar el entorno virtual
deactivate


# Crear archivo de configuración del socket de Gunicorn
sudo bash -c "cat > /etc/systemd/system/gunicorn.socket <<EOF
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
EOF"


# Crear archivo de configuración para gunicorn
sudo bash -c "cat > /etc/systemd/system/gunicorn.service <<EOF
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=$usuario
Group=www-data
WorkingDirectory=/home/$usuario/$nombre_proyecto
ExecStart=/home/$usuario/$nombre_proyecto/$entorno_virtual/bin/gunicorn \\
          --access-logfile - \\
          --workers 3 \\
          --bind unix:/run/gunicorn.sock \\
          $proyecto.wsgi:application

[Install]
WantedBy=multi-user.target
EOF"

# Iniciar y habilitar el socket de Gunicorn
sudo systemctl start gunicorn.socket

# Habilitar el socket de Gunicorn
sudo systemctl enable gunicorn.socket

# Verificar el estado del socket de Gunicorn
sudo systemctl status gunicorn.socket

# Habilitar y arrancar el servicio de Gunicorn
sudo systemctl daemon-reload

# Iniciar el servicio de Gunicorn
sudo systemctl restart gunicorn


# Crear archivo de configuración en Nginx usando las variables
sudo bash -c "cat > /etc/nginx/sites-available/$nombre_proyecto <<EOF
server {
    listen 80;
    server_name $server_ip;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /staticfiles/ {
        root /home/$usuario/$nombre_proyecto;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
EOF"

#Activating the Nginx Server Block
sudo ln -s /etc/nginx/sites-available/$nombre_proyecto /etc/nginx/sites-enabled

#Testing the Nginx Configuration File
sudo nginx -t

#Restarting Nginx
sudo systemctl restart nginx

# Configurar el firewall
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'

echo "Despliegue del proyecto $nombre_proyecto completado."