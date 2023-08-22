import boto3

# Create a Boto3 IAM client
iam_client = boto3.client('iam')

# Specify the IAM user whose access keys you want to list
username = 'eksctl'

# List access keys
response = iam_client.list_access_keys(UserName=username)
access_keys = response['AccessKeyMetadata']
print("Access keys:", access_keys)
