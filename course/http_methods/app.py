from flask import Flask, make_response, jsonify, request, render_template

app = Flask(__name__)

stock = {
    "fruit":{
        "apple":30,
        "banana":45,
        "cherry":1000
    }
}

# GET 
# POST
# PUT
# PATCH
# DELETE

@app.route("/get-text")
def get_text():
    return "some text"

@app.route("/qs")
def qs():
    if request.args:
        req = request.args
        return " ".join(f"{k}: {v} " for k, v in req.items())

    return "No query"

@app.route("/stock")
def get_stock():
    res = make_response(stock, 200)

    return res

@app.route("/stock/<collection>")
def get_collection(collection):

    """Returns the collection from stock"""
    if collection in stock:
        res = make_response(jsonify(stock[collection]), 200)

        return res

    res =  make_response(jsonify({"error":"Item not found"}), 400)

    return res

# Get a collection member
@app.route("/stock/<collection>/<member>")
def get_member(collection, member):
    """Returns the qty of the member"""

    if collection in stock:
        member = stock[collection].get(member)
        if member:
            res = make_response(jsonify(member), 200)
            return res

        res = make_response(jsonify({"error":"Unknown member"}), 400)
        return res

    res = make_response(jsonify({"error": "collection not found"}), 400)
    return res