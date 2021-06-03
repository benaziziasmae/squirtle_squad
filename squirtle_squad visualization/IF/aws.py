from config import aws_access_key_id, aws_secret_access_key
import boto3


# a request to boto3
s3 = boto3.resource(
    service_name='s3',
    region_name='ca-central-1',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)