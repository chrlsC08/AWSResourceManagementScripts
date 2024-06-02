import boto3

def stop_ec2_instance(instance_id):
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Stop the EC2 instance
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f'Stopping EC2 instance {instance_id}')

if __name__ == '__main__':
    # Specify your instance ID
    instance_id = 'insert instance id'
    
    # Call the function to stop the EC2 instance
    stop_ec2_instance(instance_id)