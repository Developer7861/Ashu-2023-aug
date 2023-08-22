import boto3

client = boto3.client('ec2')

instances-ids = ["i-0fcd4aa81710c4a59"]

response = client.start_instance(Instance=instances-ids)

print(response)