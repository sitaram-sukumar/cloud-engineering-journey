import boto3
oS3 = boto3.client("s3")
response = oS3.list_buckets()

print("*"*90)
print(f'{"Bucket Name":35} {"Region":25}  {"Creation Date"} ' )
print("*"*90)
iCount = 0;
sBuckLoc = ""
for bucket in response["Buckets"]:
    #print(f'{bucket["Name"].upper():35} {bucket["BucketArn"]:25} {bucket["CreationDate"]}')
    r1 = oS3.get_bucket_location(Bucket=bucket["Name"])
    sBuckLoc = r1["LocationConstraint"]
    print(f'{bucket["Name"].upper():35} {sBuckLoc:25} {bucket["CreationDate"]} ')
    if iCount == 0:
        iCount=1
        # print("type(buck)", type(bucket))
        # print("buck.keys()", bucket.keys())
        # print("buck[CreationDate]", type(bucket["CreationDate"]))
        # print("dir(buck)", dir(bucket))
        r1 = oS3.get_bucket_location(Bucket=bucket["Name"])
        sBuckLoc = r1["LocationConstraint"]

print("*"*90)
     #print("help(buck)", help(bucket))
