#!/bin/bash

# Especifica la información de conexión de la base de datos
DB_HOST="localhost"
DB_PORT="5432"
DB_NAME="gcp_poc"
DB_USER="fabio"
DB_PASSWORD="fabio"

# Especifica el nombre del archivo CSV de salida
OUTPUT_FILE="resultado_nuevo.csv"

FILTER="'A granel'"

# Ejecuta la consulta SQL y guarda el resultado en el archivo CSV
echo "Ejecutando consulta SQL..."
psql -h $DB_HOST -p $DB_PORT -d $DB_NAME -U $DB_USER -c "COPY (select * from onpremise.categorias c where category_name = $FILTER) TO STDOUT DELIMITER '|' CSV HEADER;" > $OUTPUT_FILE

echo "Archivo generado: $OUTPUT_FILE"
echo "Copiando archivo a GCS..."
gsutil cp $OUTPUT_FILE gs://poc-gcp-20230323/uploaded_data/20230323/;

