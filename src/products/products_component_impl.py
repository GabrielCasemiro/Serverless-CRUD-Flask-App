from .products_component import AbstractProduct
from .s3_products_repository import S3ProductsRepository

class ProductsImpl(AbstractProduct):
    def __init__(self) -> None:
        self.repository_obj = S3ProductsRepository(bucket_name="products-api-buckets3")

    def create_product(self, product):
        product_id = self.repository_obj.create_product(product)
        return product_id

    def get_product(self, product_id):
        product = self.repository_obj.get_product(product_id)
        return product

    def update_product(self, product_id, product):
        product_id = self.repository_obj.update_product(product_id, product)
        return product_id

    def delete_product(self, product_id):
        self.repository_obj.delete_product(product_id)
        return

    def get_all_products(self):
        products = self.repository_obj.get_all_products()
        return products