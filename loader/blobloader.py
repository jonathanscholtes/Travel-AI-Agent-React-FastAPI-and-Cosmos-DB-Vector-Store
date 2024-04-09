from os import environ
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv(override=True)


class BlobLoader():

    def __init__(self):
        connection_string = environ.get("AZURE_STORAGE_CONNECTION_STRING")

        # Create the BlobServiceClient object        
        self.blob_service_client =  BlobServiceClient.from_connection_string(connection_string)


    def load_binay_data(self,data, blob_name:str, container_name:str):     

        blob_client = self.blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # Upload the blob data - default blob type is BlockBlob
        blob_client.upload_blob(data,overwrite=True)