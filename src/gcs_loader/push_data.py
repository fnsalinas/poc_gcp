
from typing import Dict, List, Dict, Any
import logging


def put_file_in_gcs(bucket_name: str, folderpath: str, filename: str, filepath: str) -> None:
    """
    Put a file in a GCS bucket.
    """
    from google.cloud import storage

    client = storage.Client()

    logging.info(f"Putting file {filename} in GCS bucket {bucket_name} and folder {folderpath}.")
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(f"{folderpath}/{filename}")
    blob.upload_from_filename(filepath)


if __name__ == "__main__":
    bucket_name: str = "poc-gcp-20230323"
    folderpath: str = "raw_data"
    filename: str = "1004_gcp_poc_onpremise_precierre.csv"
    filepath: str = "/home/ubuntu/workspace/fsalinas/TMP_DATA/1004_gcp_poc_onpremise_precierre.csv"
    put_file_in_gcs(bucket_name, folderpath, filename, filepath)
