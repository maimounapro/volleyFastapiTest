import os
import logging
import boto3
from botocore.exceptions import ClientError
from API.config.settings import settings


async def upload_file_into_s3(image_path, bucket=settings.BUCKET_NAME, object_name=None, **kwargs):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(image_path)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(image_path, bucket, object_name, ExtraArgs={"Metadata": 
                                                                                        {"tournoi_id": kwargs["tournoi_id"]},
                                                                                    "ContentType": "image/jpeg"})
    except ClientError as e:
        logging.error(e)
        return False
    return True
    
def get_object_url(object_name, bucket=settings.BUCKET_NAME):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket, 'Key': object_name})
        return response
    except ClientError as e:
        logging.error(e)
        return None