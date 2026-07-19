import boto3
oIAM = boto3.client("iam");

def main():
	response = oIAM.list_users()
	print(type(response))
	print(response.keys())
	print("type(response[Users])", type(response["Users"]))
	print("len of users->", len(response["Users"]))
	for eaUsr in response["Users"]:
		print(eaUsr["UserName"], eaUsr["UserId"], eaUsr["Arn"], eaUsr["CreateDate"])
		print("-"*40)

if __name__=="__main__":
	main()
