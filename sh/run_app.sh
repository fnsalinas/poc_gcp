#!/bin/bash

# create the environment variables
export APP_MAIN_PATH="/home/ubuntu/workspace/fsalinas/poc_gcp"
export GOOGLE_APPLICATION_CREDENTIALS="/home/ubuntu/workspace/fsalinas/PRIVATE/gcp_sa/gcp_poc/poc-gcp-381517-646d17edc845.json"
export GOOGLE_CLOUD_PROJECT="poc-gcp-381517"
export TMP_DAT_FOLDER="/home/ubuntu/workspace/fsalinas/TMP_DATA"

mkdir -p $TMP_DAT_FOLDER;

# run the app in the virtual environment
cd $APP_MAIN_PATH;
pipenv run python3 app.py;
