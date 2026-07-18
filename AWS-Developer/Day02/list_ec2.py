import boto3
oEC2 = boto3.client("ec2")
response = oEC2.describe_instances()
print(type(response))
print(response.keys())

