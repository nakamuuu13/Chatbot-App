from flask import Flask, jsonify, request, Response, stream_with_context
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/api/helloworld", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello, World!"})