#!/bin/sh
WEBSITE_DIR="/home/pi/Desktop/rasberryWebsite3"
SUPERVISOR_CONF_FILE="local_webserver.conf"
PENV="$WEBSITE_DIR/env/bin/python3"
PIPENV="$WEBSITE_DIR/env/bin/pip"
echo '============ pull from git:'
cd $WEBSITE_DIR
sudo git pull
sudo su
echo '============ install requirements.txt:'
$PIPENV install -r $WEBSITE_DIR/requirements.txt
echo '============ migrate:'
$PENV $WEBSITE_DIR/website/manage.py migrate
echo '============ update supervisor:'
su pi
sudo supervisorctl update
sudo supervisorctl restart local_webserver
sudo supervisorctl status