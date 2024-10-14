from flask import Flask, jsonify, request, Response, stream_with_context
from flask_cors import CORS

from modules.chat.open_ai_chat import OpenAIChatResponse
from modules.vectorstore.vectorstore import VectorstoreManager
from modules.document_structuring.document_structuring import DocumentStructuring


app = Flask(__name__)
CORS(app)

@app.route("/api/helloworld", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello, World!"})

@app.route("/api/chat/create_response_gpt_4o_mini", methods=["POST"])
def create_response():
    try :
        data: dict = request.get_json()
        input_text: str = data["text"]
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
        name: str = request.form.get("name")
        description: str = request.form.get("description")

        files: list = request.files.getlist("files")

        # VectorstoreManager.create_vectorstore(
        #     files=files,
        #     name=name,
        #     description=description
        # )
        DocumentStructuring.invoke(
            files=files,
            name=name
        )


        return jsonify({"message": "Created vectorstore"})
    except Exception as e:
        print(e)
        return Response("Error from create_vectorstore", status=500)

@app.route("/api/vectorstore/list_vectorstores", methods=["GET"])
def list_vectorstores():
    try :
        None
    except Exception as e:
        print(e)
        return Response("Error from list_vectorstores", status=500)
    
@app.route("/api/vectorstore/delete_vectorstore", methods=["POST"])
def delete_vectorstore():
    try :
        None
    except Exception as e:
        print(e)
        return Response("Error from delete_vectorstore", status=500)
    
@app.route("/api/vectorstore/search_vectorstore", methods=["POST"])
def search_vectorstore():
    try :
        data: dict = request.get_json()
        name: str = data["name"]
        query: str = data["query"]

        search_results = VectorstoreManager.search_vectorstore(
            name=name,
            query=query
        )

        response = search_results

        return jsonify(response)
    except Exception as e:
        print(e)
        return Response("Error from search_vectorstore", status=500)

@app.route("/api/test", methods=["GET"])
def create_document_structuring():
    try :
        resuponse = DocumentStructuring.invoke()
        
        return jsonify(resuponse)
    except Exception as e:
        print(e)
        return Response("Error from create_document_structuring", status=500)