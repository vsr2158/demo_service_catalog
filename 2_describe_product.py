import boto3
import pprint

ProductId = input('Product_id: ')
# Create a Service Catalog client
sc_client = boto3.client('servicecatalog')

# List all products
response = sc_client.describe_product(Id = ProductId)
pprint.pprint(response)
print('+++++++++++++++++++++++++++++++++++++++++++++++')

ProductId = response["ProductViewSummary"]["ProductId"]
ProvisioningArtifactId = response["ProvisioningArtifacts"][0]["Id"]
LaunchPaths_name = response["LaunchPaths"][0]["Name"]
response = sc_client.describe_provisioning_parameters(ProductId = ProductId,ProvisioningArtifactId = ProvisioningArtifactId, PathName= LaunchPaths_name)
pprint.pprint(response)
