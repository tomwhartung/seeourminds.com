#!/bin/bash
#
# run.sh: tiny shell script to run the development server for this app
# --------------------------------------------------------------------
#
# Setting RUNNING_LOCALLY does the following:
# - causes site to display grey boxes instead of ads
# - enables the tiny sized quiz (containing 4 questions for testing) option
# - turns on the django DEBUG option (in settings.py)
#   (this is NOT the same as DJANGO_DEBUG)
#
# Setting DJANGO_DEBUG does the following:
# - prints detailed information about how quizzes are scored
#

# export DJANGO_DEBUG=1

export RUNNING_LOCALLY=1
export PYTHONPATH="..:${PYTHONPATH}"
python3 -m manage runserver 0.0.0.0:8001
