
from google.cloud import bigquery_datatransfer_v1
from google.protobuf.json_format import MessageToJson
from google.protobuf.struct_pb2 import Struct

from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('path/to/service_account.json')


client = bigquery_datatransfer_v1.DataTransferServiceClient(credentials=credentials)

source_project_id = "my-source-project-id"
destination_project_id = "my-destination-project-id"

transfer_config = {
    "destination_dataset_id": "my-destination-dataset-id",
    "display_name": "My Transfer Job",
    "data_source_id": "google_cloud_storage",
    "params": {
        "destination_table_name_template": "my_table",
        "bucket_name": "my_bucket",
        "object_path": "my_path",
    },
    "schedule": "every 24 hours",
    "data_refresh_window_days": 0,
    "notification_pubsub_topic": None,
}

transfer_config = bigquery_datatransfer_v1.types.TransferConfig(**transfer_config)
created_config = client.create_transfer_config(
    parent=f"projects/{destination_project_id}",
    transfer_config=transfer_config,
)

response = client.start_manual_transfer_runs(
    parent=f"projects/{destination_project_id}/transferConfigs/{created_config.name}",
    requested_time_range={
        "start_time": {
            "seconds": int(start_time.timestamp()),
        },
        "end_time": {
            "seconds": int(end_time.timestamp()),
        },
    },
)

