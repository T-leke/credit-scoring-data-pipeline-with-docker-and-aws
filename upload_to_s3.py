import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Fetch credentials from environment variables
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = "creditscoredata17"  # Replace with your S3 bucket name
OUTPUT_FOLDER = "output"  # Local folder containing the CSV file
FILE_NAME = "bank_data.csv"  # CSV file name

#Initialize S3 client using environmental variables
s3_client = boto3.client(
    "s3",
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_KEY
)

def upload():
    file_path = os.path.join(OUTPUT_FOLDER, FILE_NAME)

    if not os.path.exists(file_path):
        print(f"file {FILE_NAME} successfully uploaded to {BUCKET_NAME}/{FILE_NAME}")
        return
    
    try:
        s3_client.upload_file(file_path, BUCKET_NAME, FILE_NAME)
        print(f"file {FILE_NAME} successfully uploaded to {BUCKET_NAME}/{FILE_NAME}")
    except Exception as e:
        print(f"failed to upload file: {e}")


if __name__ == "__main__":
    upload()
