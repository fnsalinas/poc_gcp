
import csv
import os
from typing import Dict, List, Tuple, Any
import psycopg2
import json
import logging

from src.common.common import (
    get_config_reader,
    get_source_sql_reader
)


def extract_postgres(process_id: int, bucket_name: str, folderpath: str, vars: Dict[str, Any] = {}) -> str:
    """
    Extract data from PostgreSQL database.
    """

    logging.info(f"Extracting data from PostgreSQL database for process_id {process_id}.")
    process_config_data: Dict[str, Any] = get_config_reader(
        process_id=process_id,
        bucket_name=bucket_name,
        folderpath=folderpath
    )

    source_type: str = process_config_data.get("source").get("type")
    if source_type.lower().strip() != "postgresql":
        raise Exception(
            f"Trying to extract data from PostgreSQL database but the source type is not PostgreSQL, is {source_type}.")
    else:
        source_config_data: Dict[str, Any] = process_config_data.get("source")

    db_config_data: Dict[str, Any] = dict(
        host=source_config_data.get("ip_dns"),
        port=source_config_data.get("port"),
        dbname=source_config_data.get("database"),
        user=source_config_data.get("user"),
        password=source_config_data.get("secret_tag")
    )

    TMP_DATA_FOLDER: str = os.environ.get("TMP_DATA_FOLDER")
    source_database: str = source_config_data.get("database")
    source_schema: str = source_config_data.get("schema")
    source_table: str = source_config_data.get("table")
    filepath: str = f"{TMP_DATA_FOLDER}/{process_id}_{source_database}_{source_schema}_{source_table}.csv"

    extraction_sql_filepath: str = source_config_data.get(
        "extraction_sql_filepath")
    sql: str = get_source_sql_reader(bucket_fullpath=extraction_sql_filepath)
    sql: str = sql.format(**vars)

    logging.info(f"SQL to extract data from PostgreSQL database for process_id {process_id} is \n{sql}")
    logging.info(f"Extracting data from PostgreSQL database for process_id {process_id} and saving it to {filepath}.")
    conn = psycopg2.connect(**db_config_data)
    cur = conn.cursor()
    with open(filepath, 'w', newline='') as output_file:
        cur.execute(sql)
        writer = csv.writer(
            output_file,
            delimiter='~',
            quotechar='"',
            doublequote=True
        )
        writer.writerow([i[0] for i in cur.description])
        writer.writerows(cur.fetchall())
        cur.close()
        conn.close()

    return filepath


if __name__=="__main__":
    filepath: str = extract_postgres(
        process_id=1004,
        bucket_name="poc-gcp-config-20230323",
        folderpath="process",
        vars={}
    )
    print(filepath)