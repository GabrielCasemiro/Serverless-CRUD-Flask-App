from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def create_product(self, product):
        pass

    @abstractmethod
    def get_product(self, product_id):
        pass

    @abstractmethod
    def update_product(self, product_id, product):
        pass

    @abstractmethod
    def delete_product(self, product_id):
        pass

    @abstractmethod
    def get_all_products(self):
        pass