import os
import ibm_boto3
from ibm_botocore.client import Config, ClientError

API_KEY = "AerehQeOtiZljYn3cp3Rv5--PTLRVXJvROW8YJib6Fd6"
SERVICE_INSTANCE_ID = "crn:v1:bluemix:public:cloud-object-storage:global:a/90f4ad63175d479a84ee05b5445012dd::"
ENDPOINT_URL = "https://s3.eu-es.cloud-object-storage.appdomain.cloud"  # Madrid

cos = ibm_boto3.client(
    "s3",
    ibm_api_key_id=API_KEY,
    ibm_service_instance_id=SERVICE_INSTANCE_ID,
    config=Config(signature_version="oauth"),
    endpoint_url=ENDPOINT_URL
)

def download_file(bucket_name, key, filename):
    try:
        cos.download_file(Bucket=bucket_name, Key=key, Filename=filename)
        print(f"Archivo '{filename}' descargado correctamente.")
    except ClientError as e:
        print(f"Error al descargar el archivo: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

BUCKET_NAME = "somebucket-for-interview"
FILE_KEY = "README.md"
OUTPUT_FILENAME = "README_downloaded.md"

download_file(BUCKET_NAME, FILE_KEY, OUTPUT_FILENAME)