import boto3
from botocore.exceptions import ClientError

from decouple import config


class AWSProvider:

    def upload_file_s3(self, way_to_save, file_path, bucket='tinde-mentoria-devaria'):

        s3_client = boto3.client(
            's3',
            aws_access_key_id=config('AWS_ACCESS_KEY'),
            aws_secret_access_key=config('AWS_SECRET_KEY'),
            region_name='us-east-2'
        )

        try:
            s3_client.upload_file(file_path, bucket, Key=way_to_save)

            url = s3_client.generate_presigned_url(
                'get_object',
                ExpiresIn=0,
                Params={'Bucket': bucket, 'Key': way_to_save}
            )

            return str(url).split('?')[0]
        except ClientError as erro:
            print(erro)
            return False

    def delete_file_S3(self, photo):

        s3_client = boto3.client(
            's3',
            aws_access_key_id=config('AWS_ACCESS_KEY'),
            aws_secret_access_key=config('AWS_SECRET_KEY'),
            region_name='us-east-2'
        )

        try:
            response = s3_client.delete_object(
                Bucket='tinde-mentoria-devaria',
                Key=f'photo-perfil/{photo}',

            )

            print(response)
        except ClientError as erro:
            print(erro)
            return False

