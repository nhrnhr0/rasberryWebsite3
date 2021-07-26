#!/bin/sh
WEBSITE_DIR="/home/pi/Desktop/rasberryWebsite3"
SUPERVISOR_CONF_FILE="local_webserver.conf"
cd $WEBSITE_DIR
sudo git pull
sudo supervisorctl update
sudo supervisorctl restart local_webserver
sudo supervisorctl status