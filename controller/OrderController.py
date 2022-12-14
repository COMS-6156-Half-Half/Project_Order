from flask import Flask, Response, request
import json
from OrderDB import OrderDB


# Create the Flask application object.
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'



@app.route("/api/record/all", methods=["GET"])
def get_all_record():

    result = OrderDB.get_all()

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/record/insert", methods=["POST"])
def insert_record():
    data = request.get_json()
    id =int(data["id"])
    seller_id = int(data["seller_id"])
    product_id = int(data["product_id"])
    buyer_id = int(data["buyer_id"])
    result = OrderDB.insert_record(id, seller_id, product_id, buyer_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/record/seller/<seller_id>", methods=["GET"])
def get_by_sellerId(seller_id):

    
    result = OrderDB.get_by_sellerId(seller_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/record/buyer/<buyer_id>", methods=["GET"])
def get_by_buyerId(buyer_id):
    
    result = OrderDB.get_by_buyerId(buyer_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/record/delete/", methods=["POST"])
def delete_by_orderId():
    data = request.get_json()
    order_id = int(data["order_id"])
    result = OrderDB.delete_by_orderId(order_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
