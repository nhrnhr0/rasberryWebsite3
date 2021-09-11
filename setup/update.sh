#!/bin/sh
WEBSITE_DIR="/home/pi/Desktop/rasberryWebsite3"
SUPERVISOR_CONF_FILE="local_webserver.conf"
PENV="$WEBSITE_DIR/env/bin/python3"
PIPENV="$WEBSITE_DIR/env/bin/pip"
echo 'RUN:'
echo '================================================================='
echo cd $WEBSITE_DIR
echo 'sudo supervisorctl stop local_webserver'
echo 'sudo git pull'
echo $PIPENV install -r $WEBSITE_DIR/requirements.txt
echo $PENV $WEBSITE_DIR/website/manage.py migrate
echo $PENV $WEBSITE_DIR/website/manage.py migrate --database=online_db
echo $PENV $WEBSITE_DIR/website/manage.py collectstatic
echo 'yes'
echo 'sudo supervisorctl start local_webserver'
echo '================================================================='





#echo '============ pull from git:'
#cd $WEBSITE_DIR
#sudo git pull
#echo '============ install requirements.txt:'
#$PIPENV install -r $WEBSITE_DIR/requirements.txt
#echo '============ migrate:'
#$PENV $WEBSITE_DIR/website/manage.py migrate
#echo '============ update supervisor:'
#sudo supervisorctl update
#sudo supervisorctl restart local_webserver
#sudo supervisorctl status
#echo 'execute this commands: '
#echo '============================================================='
#echo $PENV $WEBSITE_DIR/website/manage.py migrate
#echo 'sudo supervisorctl update'
#echo 'sudo supervisorctl restart'
#echo '============================================================='
