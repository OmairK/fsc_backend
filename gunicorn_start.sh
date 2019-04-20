#!/bin/bash

NAME="fsic"                              #Name of the application (*)
DJANGODIR=/home/fsc/server/fsc_backend/fsic             # Django project directory (*)
SOCKFILE=/home/fsc/server/fsc_backend/run/gunicorn.sock        # we will communicate using this unix socket (*)
USER=fsc                                        # the user to run as (*)
GROUP=webdata                                     # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=fsic.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=fsic.wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/fsc/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/fsc/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE

