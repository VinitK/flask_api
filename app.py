from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        "name":"Store1",
        "items":[
            {
                "name":"Item1",
                "price":10
            },
            {
                "name":"Item2",
                "price":20
            }
        ]
    },
    {
        "name":"Store2",
        "items":[
            {
                "name":"Item3",
                "price":20
            },
            {
                "name":"Item4",
                "price":20
            }
        ]
    }
]

#GET HOME
@app.route('/')
def home():
    return "Hello World!"

#GET STORES
@app.route('/stores')
def get_stores():
    return jsonify({'stores':stores})

#POST STORE
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(stores)

#GET STORE BY NAME
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message":"store not found"})

#POST ITEM IN STORE
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"]==name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store["items"].append(new_item)
            return jsonify(store)
    return jsonify({"message":"Store not found"})

#GET ITEMS IN STORE
@app.route('/store/<string:name>/items')
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items":store["items"]})
    return jsonify({"message": "store not found"})

app.run(port=5000)