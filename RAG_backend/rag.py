import os
from connectDB import get_connection

# Step 1: Collect Data

folder_path = os.path.join(os.path.dirname(__file__), '..', 'data')  # Add your files here


# Step 2: Preprocess Data
documents = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
            documents.append((f.name, f.read()))
print(documents)
#3. Create Embeddings

from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_openai import OpenAIEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# vector_store = PostgresVector(
#     connection_string=DATABASE_URL,
#     embedding_dimension=1536,  # Adjust based on your embedding model
#     table_name="documents"
# )

# vector_store.add_texts(
#     texts=[doc[1] for doc in documents],
#     metadatas=[doc[0] for doc in documents],
#     embedding=embedding_model
# )

# file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'source.txt')
