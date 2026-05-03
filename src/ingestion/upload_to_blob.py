import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient


def upload_file_to_blob(local_file_path, container_name, blob_name):
    blob_service_client = BlobServiceClient.from_connection_string(
        os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    )

    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )

    with open(local_file_path, "rb") as file:
        blob_client.upload_blob(file, overwrite=True)

    print(f"Uploaded {local_file_path} to container '{container_name}'")


def main():
    load_dotenv()

    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    raw_container = os.getenv("AZURE_STORAGE_RAW_CONTAINER")
    processed_container = os.getenv("AZURE_STORAGE_PROCESSED_CONTAINER")

    if not connection_string:
        raise ValueError("AZURE_STORAGE_CONNECTION_STRING is missing")

    upload_file_to_blob(
        local_file_path="data/raw/sample_response.json",
        container_name=raw_container,
        blob_name="sample_response.json"
    )

    upload_file_to_blob(
        local_file_path="data/processed/processed_post.csv",
        container_name=processed_container,
        blob_name="processed_post.csv"
    )

    print("Upload completed successfully.")


if __name__ == "__main__":
    main()