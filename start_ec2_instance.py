import boto3

def start_ec2_instance(instance_id):
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Start the EC2 instance
    ec2.start_instances(InstanceIds=[instance_id])
    print(f'Starting EC2 instance {instance_id}')

if __name__ == '__main__':
    # Specify your instance ID
    instance_id = 'insert instance id'
    
    # Call the function to start the EC2 instance
    start_ec2_instance(instance_id)