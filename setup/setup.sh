#!/bin/sh

WEBSITE_DIR = "/home/pi/Desktop/rasberryWebsite3/"
SUPERVISOR_CONF_FILE = "local_webserver.conf"
echo '============ done setting up variables'
sudo apt-get install supervisor
sudo cp $WEBSITE_DIR/setup/$SUPERVISOR_CONF_FILE /etc/supervisor/conf.d/$SUPERVISOR_CONF_FILE
echo '============ done supervisor install and conf file copy'

python3 -m venv $WEBSITE_DIR/env
echo '============ done create env'
$WEBSITE_DIR/env/bin/pip install -r $WEBSITE_DIR/requirements.txt
echo '============ done install requirements.txt'

echo '============ updating supervisor'
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl status

echo '============ done updating supervisor'