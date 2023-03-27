
from typing import Dict, List, Dict, Any


def put_file_in_gcs(bucket_name: str, folderpath: str, filename: str, filepath: str) -> None:
    """
    Put a file in a GCS bucket.
    """
    from google.cloud import storage

    client = storage.Client()

    bucket = client.bucket(bucket_name)
    blob = bucket.blob(f"{folderpath}/{filename}")
    blob.upload_from_filename(filepath)


if __name__ == "__main__":
    bucket_name: str = "poc-gcp-config-20230323"
    folderpath: str = "process"
    filename: str = "test.txt"
    filepath: str = "/home/ubuntu/workspace/fsalinas/TMP_DATA/gcp_poc_onpremise_categorias_1000.csv"
    put_file_in_gcs(bucket_name, folderpath, filename, filepath)
