import boto3
import pprint

# Create a Service Catalog client
sc_client = boto3.client('servicecatalog')

# List all products
response = sc_client.search_products()

pprint.pprint(response)
