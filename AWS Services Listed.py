# Creating an empty list with the name "awsservices"


awsservices = []

# Inserting elements in the list

awsservices.append("Python")
awsservices.append("S3")
awsservices.append("Lambda")
awsservices.append("EC2")
awsservices.append("VPC")
awsservices.append("Nat Gateway")
awsservices.append("DynamoDB")
awsservices.append("KMS")

#print item list and length

print("Items of list are:", awsservices)
print("Length of List:", len(awsservices))

Items of list are: ['Python', 'S3', 'Lambda', 'EC2', 'VPC', 'Nat Gateway', 'DynamoDB', 'KMS']
Length of List: 8


#del removes an items based on its index value

del awsservices[0]
print(awsservices)

del awsservices[3]
print(awsservices)

#Print New item list and length
print("Items of list are:", awsservices)
print("Length of List:", len(awsservices))





