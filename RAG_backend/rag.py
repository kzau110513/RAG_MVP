import os
# from connectDB import get_connection
from langchain_postgres import PGVector

# Step 1: Collect Data

folder_path = os.path.join(os.path.dirname(__file__), 'data')  # Add your files here


# Step 2: Preprocess Data
documents = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
            documents.append((f.read(), os.path.basename(f.name)))
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

#4. Add Documents to Vector Store
from langchain_core.documents import Document
documents = [Document(id=documents[i][1], page_content=documents[i][0], metadata={"source": documents[i][1]}) for i in range(len(documents))]
# documents = [Document(page_content=documents[i][0], metadata={"source": documents[i][1]}) for i in range(len(documents))]
# print(documents)
vector_store.add_documents(documents)

#5. Get Document by ID
print(vector_store.get_by_ids([document.id for document in documents]))

#6. Query the Vector Store
# results = vector_store.similarity_search(query="what about the climate change",k=1)
# for doc in results:
#     print(f"* {doc.page_content} [{doc.metadata}]")

#7. Delete the Collection
# vector_store.delete_collection()
# vector_store.delete(ids=["climate_change.txt"])



