
from typing import Dict, List, Tuple, Any
import json
from glob import glob
import psycopg2
import csv
import subprocess
from datetime import datetime

# subprocess.run(['export', 'GOOGLE_APPLICATION_CREDENTIALS=/home/ubuntu/workspace/fsalinas/PRIVATE/gcp_sa/gcp_poc/poc-gcp-381517-646d17edc845.json'])
# export GOOGLE_APPLICATION_CREDENTIALS=/home/ubuntu/workspace/fsalinas/PRIVATE/gcp_sa/gcp_poc/poc-gcp-381517-646d17edc845.json

### Inicio codigo para conectar con BigQuery

from google.cloud import bigquery

# Crea un objeto cliente de BigQuery
client = bigquery.Client()

# Define los detalles de la tabla que se va a crear
table_id = 'poc-gcp-381517.poc_gcp.TEST'
schema = [
    bigquery.SchemaField('column1', 'STRING'),
    bigquery.SchemaField('column2', 'INTEGER'),
]

# Define la consulta de DDL para crear la tabla
query = f'CREATE TABLE {table_id} ({", ".join([f"{field.name} {field.field_type}" for field in schema])})'

# Ejecuta la consulta
query_job = client.query(query)

# Espera a que el trabajo de consulta se complete
query_job.result()

# Imprime un mensaje de confirmación
print(f'La tabla {table_id} ha sido creada en el dataset.')

### Fin codigo para conectar con BigQuery

def load_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as f:
        return json.load(f)


folder_path: str = "/home/ubuntu/workspace/fsalinas/poc_gcp/config/*"

json_files: List[str] = sorted(glob(folder_path))

json_data_list: List[Dict[str, Any]] = [load_json(file_path) for file_path in json_files]

print(json.dumps(json_data_list, indent=4))

json_data: Dict[str, Any] = json_data_list[0]
table_name: str = json_data['table_name_source']
table_schema: str = json_data['table_schema_source']


# Especifica la información de conexión de la base de datos
db_host = "localhost"
db_port = "5432"
db_name = "gcp_poc"
db_user = "fabio"
db_password = "fabio"

# Crea la conexión a la base de datos
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)

# Especifica la consulta SQL
sql = f"select * from {table_schema}.{table_name} c"

dt = datetime.now().strftime('%Y%m%d%H%M%S')
filename = f'{dt}_resultado_python.csv'

# Ejecuta la consulta SQL y guarda los resultados en un archivo CSV
with open(filename, 'w', newline='') as f:
    cur = conn.cursor()
    cur.execute(sql)
    writer = csv.writer(f, delimiter='|')
    writer.writerow([i[0] for i in cur.description])
    writer.writerows(cur.fetchall())
    cur.close()

# Cierra la conexión a la base de datos
conn.close()

# Sube el archivo a Google Cloud Storage con gsutil
bucket_name = 'poc-gcp-20230323'
folder_path = 'uploaded_data/20230323/'
subprocess.run(['gsutil', 'cp', filename, f'gs://{bucket_name}/{folder_path}'])

