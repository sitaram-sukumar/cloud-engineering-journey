import boto3
oEC2 = boto3.client("ec2")
response = oEC2.describe_instances()
print(type(response))
print(response.keys())
print(type(response["Reservations"]))
print(len(response["Reservations"]))
for eaReservation in response["Reservations"]:
	print("eaReservation", type(eaReservation))
	print(eaReservation.keys())
	print("type-> reservation[Instances]", type(eaReservation["Instances"]))
	for eaInst in eaReservation["Instances"]:
		print("type-> eaInst", type(eaInst))
		## print(eaInst.keys())
		print("Instance Id-> ", eaInst["InstanceId"])
