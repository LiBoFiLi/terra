import boto3
import os

s3 = boto3.client('s3', endpoint_url='http://localhost:4566')

def lambda_handler(event, context):
    source_bucket = os.environ['SOURCE_BUCKET']
    destination_bucket = os.environ['DESTINATION_BUCKET']

    for record in event['Records']:
        key = record['s3']['object']['key']
        copy_source = {'Bucket': source_bucket, 'Key': key}
        s3.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=key)
        s3.delete_object(Bucket=source_bucket, Key=key)