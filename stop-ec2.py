import boto3

# Create a Boto3 EC2 client
ec2_client = boto3.client('ec2', region_name='us-east-2')

# Specify the instance IDs you want to start or stop
instance_ids = ['i-0fcd4aa81710c4a59']


# Stop instances
response_stop = ec2_client.stop_instances(InstanceIds=instance_ids)
print("Instances stopped:", response_stop)
