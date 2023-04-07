
from typing import Dict, List, Tuple, Any
import json
import os
import logging

# load GOOGLE_APPLICATION_CREDENTIALS on the fly
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/ubuntu/workspace/fsalinas/PRIVATE/gcp_sa/gcp_poc/poc-gcp-381517-646d17edc845.json"
os.environ["TMP_DATA_FOLDER"] = "/home/ubuntu/workspace/fsalinas/TMP_DATA"


def get_config_reader(process_id: int, bucket_name: str, folderpath: str) -> Dict[str, Any]:
    """
    Read the configuration file and return the configuration data.
    """
    folderpath: str = folderpath[:-1] if folderpath[-1] == "/" else folderpath
    filename: str = f"{folderpath}/{process_id}_table_config.json"
    
    from google.cloud import storage

    client = storage.Client()

    logging.info(f"Reading configuration file from GCS bucket {bucket_name} and folder {folderpath} with filename {filename}.")
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(filename)
    content = blob.download_as_string()
    config_data = json.loads(content)
    
    return config_data

def get_source_sql_reader(bucket_fullpath: str) -> str:
    """
    Read the configuration file and return the configuration data.
    """
    bucket_name: str = bucket_fullpath.replace("gs://", "").split("/")[0]
    folderpath: str = "/".join(bucket_fullpath.replace("gs://", "").split("/")[1:])
    folderpath: str = folderpath[:-1] if folderpath[-1] == "/" else folderpath
    folderpath: str = folderpath if ".sql" not in folderpath else ""
    filename: str = bucket_fullpath.replace("gs://", "").split("/")[-1]
    filepath: str = folderpath + "/" if folderpath else "" + filename
    
    from google.cloud import storage

    client = storage.Client()

    logging.info(f"Reading SQL file from GCS bucket {bucket_name} and folder {folderpath} with filename {filename}.")
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(filepath)
    sql_content = blob.download_as_string().decode("utf-8")
    
    return sql_content


