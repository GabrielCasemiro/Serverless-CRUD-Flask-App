from .products_repository import AbstractProductRepository
import uuid
import uuid
import boto3
import json

class S3ProductsRepository(AbstractProductRepository):
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3')

    def generate_product_id(self):
        return str(uuid.uuid4())

    def create_product(self, product):
        product_id = self.generate_product_id()
        product["id"] = product_id
        key = f"products/{product_id}.json"
        self.s3_client.put_object(
            Body=json.dumps(product),
            Bucket=self.bucket_name,
            Key=key
        )
        return product_id

    def get_product(self, product_id):
        key = f"products/{product_id}.json"
        response = self.s3_client.get_object(
            Bucket=self.bucket_name,
            Key=key
        )
        product_data = response['Body'].read()
        return product_data

    def update_product(self, product_id, product):
        key = f"products/{product_id}.json"
        self.s3_client.put_object(
            Body=json.dumps(product),
            Bucket=self.bucket_name,
            Key=key
        )
        return product_id

    def delete_product(self, product_id):
        key = f"products/{product_id}.json"
        self.s3_client.delete_object(
            Bucket=self.bucket_name,
            Key=key
        )
        return 

    def get_all_products(self):
        objects = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
        product_list = []
        if 'Contents' in objects:
            for obj in objects['Contents']:
                key = obj['Key']
                if key.startswith('products/') and key.endswith('.json'):
                    response = self.s3_client.get_object(Bucket=self.bucket_name, Key=key)
                    product_data = response['Body'].read()
                    product = json.loads(product_data)
                    product_list.append(product)
        return product_list