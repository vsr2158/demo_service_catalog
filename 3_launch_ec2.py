import boto3
import uuid

ProductId = input('ProductId : ')
provisionedProductName = input("provisionedProductName : ")
ProvisioningArtifactId = input("ProvisioningArtifactId : ")
PathId = input("PathId : ")

ProvisioningParameters= [
    {
      "Value": "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2",
      "Key": "LatestAmiId"
    },
    {
      "Value": "0.0.0.0/0",
      "Key": "SshAccessCidr"
    },
    {
      "Value": "t2.micro",
      "Key": "SshInstanceType"
    },
    {
      "Value": "subnet-0aab2c5008f411601",
      "Key": "Subnet"
    },
    {
      "Value": "vpc-02315075bbe7c978e",
      "Key": "Vpc"
    }
  ]

# Create a Service Catalog client
sc_client = boto3.client('servicecatalog')


response = sc_client.provision_product(
    ProductId=ProductId,
    ProvisioningArtifactId=ProvisioningArtifactId,
    PathId=PathId,
    ProvisionedProductName=provisionedProductName,
    ProvisioningParameters=ProvisioningParameters
)

print(response)
