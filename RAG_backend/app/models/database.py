from langchain_huggingface import HuggingFaceEmbeddings
from langchain_postgres import PGVector
from app.config import Config
from langchain_core.documents import Document

# embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# vector_store = PGVector(
#         connection=Config.DATABASE_URL,
#         embeddings=HuggingFaceEmbeddings(model_name=Config.MODEL_NAME),  # Adjust based on your embedding model
#         collection_name="documents",
#         use_jsonb=True,
#     )

class VectorStore:
    vector_store = None
    
    def __init__(self):
        self.vector_store = PGVector(
            connection=Config.DATABASE_URL,
            embeddings=HuggingFaceEmbeddings(model_name=Config.MODEL_NAME),
            collection_name="documents",
            use_jsonb=True,
        )

    def similarity_search_vector_db(self, query, k=1):
        return self.vector_store.similarity_search(query, k=k)

    def add_documents(self, documents: list[Document]):
        self.vector_store.add_documents(documents)
        return None

    def clear_vector_db(self, ids=None):
        self.vector_store.delete(ids=ids)
        return None

# def similarity_search_vector_db(query,k=1):
#     return vector_store.similarity_search(query, k=k)

# def add_documents(documents: list[Document]):
#     vector_store.add_documents(documents)
#     print(documents)
#     return None

# def clear_vector_db():
#     vector_store.delete_collection()
#     return None