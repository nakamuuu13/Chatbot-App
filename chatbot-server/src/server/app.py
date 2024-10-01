from flask import Flask, jsonify, request, Response, stream_with_context
from flask_cors import CORS

from modules.chat.open_ai_chat import OpenAIChatResponse
from modules.vectorstore.vectorstore import VectorstoreManager


app = Flask(__name__)
CORS(app)

@app.route("/api/helloworld", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello, World!"})


@app.route("/api/chat/create_response_gpt_4o_mini", methods=["POST"])
def create_response():
    try :
        data = request.get_json()
        input_text = data["text"]
        # model_name = data["model_name"]
        # max_tokens = data["max_tokens"]
        # temperature = data["temperature"]
        # response = ChatResponse.create_response(input_text, model_name, max_tokens, temperature)
        return Response(stream_with_context(OpenAIChatResponse.create_response_gpt_4o_mini(input_text)), mimetype="text/event-stream")
    except Exception as e:
        print(e)
        response = Response("Error from create_response", status=500)
        return response

@app.route("/api/vectorstore/create_vectorstore", methods=["POST"])
def create_vectorstore():
    try :
        None
    except Exception as e:
        print(e)
        response = Response("Error from create_vectorstore", status=500)
        return response