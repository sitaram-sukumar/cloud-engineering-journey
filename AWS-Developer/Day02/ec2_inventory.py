import boto3

def main():
	response = ec2.describe_instances()
	print(response.keys())

if __name__ == "__main__":
	main()
