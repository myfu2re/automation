import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')
s3 = boto3.client('s3', region_name='us-east-1')
lambda_client = boto3.client('lambda', region_name='us-east-1')
iam = boto3.client('iam', region_name='us-east-1')

def create_ec2_instance():
    try:
        response = ec2.run_instances(
            ImageId='ami-0abcd1234efgh5678',
            InstanceType='t2.micro',
            KeyName='your-key-name',
            MinCount=1,
            MaxCount=1
        )
        print("EC2 instance created successfully. Instance ID:", response['Instances'][0]['InstanceId'])
    except Exception as e:
        print("Error creating instance:", e)

def create_s3_bucket(bucket_name):
    try:
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': 'us-east-1'}
        )
        print(f"S3 bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print("Error creating S3 bucket:", e)

def upload_file_to_s3(bucket_name, file_path, object_name):
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"The file '{file_path}' has been uploaded to bucket '{bucket_name}' as '{object_name}'.")
    except Exception as e:
        print("Error uploading file to S3", e)

def create_lambda_function(function_name, role_arn, zip_file_path, handler_name):
    try:
        with open(zip_file_path, 'rb') as f:
            zipped_code = f.read()
        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.8',
            Role=role_arn,
            Handler=handler_name,
            Code={'ZipFile': zipped_code},
            Timeout=15,
            MemorySize=128
        )
        print(f"Lambda function '{function_name}' created successfully.")
    except Exception as e:
        print("Error creating Lambda function:", e)

def create_iam_user(user_name):
    try:
        response = iam.create_user(UserName=user_name)
        print(f"IAM user '{user_name}' created successfully.")
    except Exception as e:
        print("Error creating user IAM:", e)

if __name__ == "__main__":
    create_ec2_instance()
    create_s3_bucket('my-unique-bucket-name')
    upload_file_to_s3('my-unique-bucket-name', 'path/to/your/file.txt', 'uploaded-file.txt')
    create_lambda_function(
        'myLambdaFunction',
        'arn:aws:iam::XXXXXXXXXXXX:role/execution_role',
        'path/to/your/lambda-function.zip',
        'lambda_function.lambda_handler'
    )
    create_iam_user('new-iam-user')
