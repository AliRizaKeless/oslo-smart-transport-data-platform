import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient


def download_file_from_blob():
    load_dotenv()

    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_STORAGE_RAW_CONTAINER")
    blob_name = "sample_response.json"
    download_path = "data/raw/downloaded_sample_response.json"

    if not connection_string:
        raise ValueError("AZURE_STORAGE_CONNECTION_STRING is missing")

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )

    with open(download_path, "wb") as file:
        file.write(blob_client.download_blob().readall())

    print(f"Downloaded {blob_name} from container '{container_name}' to {download_path}")


if __name__ == "__main__":
    download_file_from_blob()