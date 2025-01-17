import os

# Step 1: Collect Data

data_files = ["data/doc1.txt", "data/doc2.txt"]  # Add your files here

# Step 2: Preprocess Data
documents = []
for file in data_files:
    with open(file, 'r', encoding='utf-8') as f:
        documents.append(f.read())

#3. Create Embeddings

from langchain.embeddings import OpenAIEmbeddings

# Initialize OpenAI embedding model
embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002")

# Create embeddings for each document
embeddings = [embedding_model.embed_query(doc) for doc in documents]
