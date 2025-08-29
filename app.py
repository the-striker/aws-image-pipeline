import boto3
from PIL import Image
import io
import json

s3 = boto3.client("s3")

def lambda_handler(event, context):
    # Extract bucket + key from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    try:
        # Download image
        file_obj = s3.get_object(Bucket=bucket, Key=key)
        img = Image.open(file_obj['Body'])

        # Resize
        img = img.resize((200, 200))

        # Save to buffer
        buffer = io.BytesIO()
        img.save(buffer, "JPEG")
        buffer.seek(0)

        # Upload to output bucket
        output_bucket = "image-pipeline-output-umesh"  # change to yours
        s3.put_object(Bucket=output_bucket, Key=key, Body=buffer)

        return {
            "statusCode": 200,
            "body": json.dumps(f"Image {key} processed successfully.")
        }

    except Exception as e:
        print("Error:", str(e))
        raise e
