import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

print("Starting Azure upload script...")

def upload_file_to_blob():
    load_dotenv()

    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_STORAGE_RAW_CONTAINER")
    local_file_path = "data/raw/sample_response.json"
    blob_name = "sample_response.json"

    if not connection_string:
        raise ValueError("AZURE_STORAGE_CONNECTION_STRING is missing")

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )

    with open(local_file_path, "rb") as file:
        blob_client.upload_blob(file, overwrite=True)

    print(f"Uploaded {local_file_path} to container '{container_name}'")


if __name__ == "__main__":
    upload_file_to_blob()