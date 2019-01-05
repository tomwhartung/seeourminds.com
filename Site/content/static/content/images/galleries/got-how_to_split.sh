#!/bin/bash
#
# List files in the groups we want to move them to
# ------------------------------------------------
#
echo 'All GOT image files:'
ls -1 20*/*.jpg
ls -1 20*/*.jpg | wc -l

echo 'House Stark:'
ls -1 20*/*stark*.jpg 20*/*snow*.jpg
ls -1 20*/*stark*.jpg 20*/*snow*.jpg | wc -l

echo 'House Baratheon:'
ls -1 20*/*baratheon*.jpg
ls -1 20*/*baratheon*.jpg | wc -l

echo 'House Lannister:'
ls -1 20*/*lannister*.jpg
ls -1 20*/*lannister*.jpg | wc -l

echo 'House Tyrell:'
ls -1 20*/*tyrell*.jpg
ls -1 20*/*tyrell*.jpg | wc -l

echo 'No specific House:'
ls -1 20*/*.jpg | grep -v baratheon | grep -v lannister | grep -v snow | grep -v stark | grep -v tyrell
ls -1 20*/*.jpg | grep -v baratheon | grep -v lannister | grep -v snow | grep -v stark | grep -v tyrell | wc -l

