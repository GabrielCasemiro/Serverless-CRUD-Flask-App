from flask import Flask, jsonify, Response, request
import os
from products.products_component_impl import ProductsImpl
import logging

app = Flask(__name__)


@app.route("/products/")
def index(methods=["GET"]):
    try:
        returned_data = products_service.get_all_products()
        return returned_data

    except Exception as ex:
        logging.exception("Fail to get products due to error %s" % str(ex))
        return Response("Fail to get products", status=500)

@app.route('/product', methods=['POST'])
def create_product():
    try:
        product = request.get_json()
        product_id = products_service.create_product(product)
        return jsonify({'product_id': product_id}), 201
    except Exception as ex:
        logging.exception("Fail to create product due to error %s" % str(ex))
        return Response("Fail to create product", status=500)


@app.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = products_service.get_product(product_id)
        return jsonify(product), 200
    except Exception as ex:
        logging.exception("Fail to get product due to error %s" % str(ex))
        return Response("Fail to get product", status=500)


@app.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        product = request.get_json()
        product_id = products_service.update_product(product_id, product)
        return jsonify({'product_id': product_id}), 200
    except Exception as ex:
        logging.exception("Fail to update product due to error %s" % str(ex))
        return Response("Fail to update product", status=500)



@app.route('/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        products_service.delete_product(product_id)
        return Response("Product deleted", status=200)
    except Exception as ex:
        logging.exception("Fail to delete product due to error %s" % str(ex))
        return Response("Fail to delete product", status=500)

products_service = ProductsImpl()
if os.environ.get("mode") == "local":
    app.run(host="127.0.0.1", port=8002)
