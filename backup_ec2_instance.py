import boto3
import datetime

# Create an EC2 client
ec2 = boto3.client('ec2')

# Specify your instance ID
instance_id = 'insert instance id'

# Create a snapshot of the instance's volume
response = ec2.create_snapshot(
    VolumeId='insert volume id',
    Description=f'Snapshot for instance {instance_id} on {datetime.datetime.now()}'
)

print(f'Snapshot created: {response["SnapshotId"]}')