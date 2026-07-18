import boto3
oEC2 = boto3.client("ec2")
response = oEC2.describe_instances()
print(type(response))
print(response.keys())
print(type(response["Reservations"]))
print(len(response["Reservations"]))
for eaReservation in response["Reservations"]:
	print("eaReservation-> ", type(eaReservation))
	print("eaReservation Keys->", eaReservation.keys())
	print("type-> reservation[Instances]->", type(eaReservation["Instances"]))
	for eaInst in eaReservation["Instances"]:
		print("type-> eaInst", type(eaInst))
		print("*"*40)
		#print(eaInst.keys())
		print("Instance Id-> ", eaInst["InstanceId"])
		print("Instance Type-> ", eaInst["InstanceType"])
		print("State-> ", eaInst["State"])
		print("Public IP-> ", eaInst["PublicIpAddress"])
		print("Private IP-> ", eaInst["PrivateIpAddress"])
		print("Instance Name->", eaInst["Tags"][0]["Value"] )
		print("AZ->", eaInst['Placement']['AvailabilityZone'] )
		print("*"*40)
		#print("##dir##", dir(eaInst));
		#print("type eaInst[Tags]->", type(eaInst["Tags"]))
		#print(eaInst["Tags"][0])

		#for eaTag in eaInst["Tags"]:
		#	print("Tag ->", type(eaTag));
		#	print("Tag Keys->", eaTag.keys())
		#	print("Instance Name", eaTag["Value"])

