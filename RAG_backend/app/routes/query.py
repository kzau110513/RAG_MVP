from flask import Blueprint, request, jsonify
from app.services.rag_service import RagService


query_bp = Blueprint("rag", __name__)

rag_service = RagService()


@query_bp.route("/query", methods=["POST"])
def query():
    data = request.json
    user_input = data.get("query", "")

    response = rag_service.process_query(user_input)

    return jsonify({"response": response})
    # process_query()
    # return jsonify({"response": "Success"})

@query_bp.route("/clear", methods=["DELETE"])
def clear():
    response = rag_service.clear_collections()
    return jsonify({"response": response})

@query_bp.route("/add_file", methods=["POST"])
def add_file():
    response = rag_service.add_file_vector()
    return jsonify({"response": response})
