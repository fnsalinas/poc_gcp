#!/bin/bash

echo "Cargando variables de entorno..."
GOOGLE_APPLICATION_CREDENTIALS=/home/ubuntu/workspace/fsalinas/poc_gcp/gcp_config/poc-gcp-381517-646d17edc845.json
APP_MAIN_PATH=/home/ubuntu/workspace/fsalinas/poc_gcp

cd $APP_MAIN_PATH;


echo "Ejecutando aplicación ETL..."
pipenv run python3 python/run_app.py

echo "Ejecución finalizada."

