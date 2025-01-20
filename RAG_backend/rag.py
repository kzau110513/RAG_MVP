import os
# from connectDB import get_connection
from langchain_postgres import PGVector

# Step 1: Collect Data

folder_path = os.path.join(os.path.dirname(__file__), '..', 'data')  # Add your files here


# Step 2: Preprocess Data
documents = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
            documents.append((f.name, f.read()))
# print(documents)
#3. Create Embeddings

from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_openai import OpenAIEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
DATABASE_URL = "postgresql+psycopg://postgres:mysecretpassword@localhost:5432/postgres"

vector_store = PGVector(
    connection=DATABASE_URL,
    embeddings=embedding_model,  # Adjust based on your embedding model
    collection_name="documents",
    use_jsonb=True,
)

# vector_store.add_texts(
#     texts=[doc[1] for doc in documents],
#     metadatas=[doc[0] for doc in documents],
#     embedding=embedding_model
# )

# file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'source.txt')
