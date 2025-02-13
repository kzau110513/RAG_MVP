# from langchain.chains import RetrievalQA
# from langchain.llms import OpenAI
# from langchain.vectorstores import FAISS
# from langchain.embeddings import OpenAIEmbeddings

# # Load vector database
# vectorstore = FAISS.load_local("faiss_index", OpenAIEmbeddings())
# retriever = vectorstore.as_retriever()
# qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=retriever)

# def process_query(query_text):
#     return qa_chain.run(query_text)

import os
from app.models.database import VectorStore
from langchain_core.documents import Document
from app.config import Config

class RagService:
    db = VectorStore()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Moves up three levels
    DATA_DIR = os.path.join(BASE_DIR, "data")

    def process_query(self, query_text):
        #5. Get Document by ID
        # print(vector_store.get_by_ids([document.id for document in documents]))

        #6. Query the Vector Store
        results = self.db.similarity_search_vector_db(query_text)
        response = []
        for doc in results:
            # print(f"* {doc.page_content} [{doc.metadata}]")
            response.append((doc.id, doc.page_content, doc.metadata))
        return response
        
        #7. Delete the Collection
        # vector_store.delete_collection()
        # vector_store.delete(ids=["climate_change.txt"])

    def add_file_vector(self):
        # Step 1: Collect Data
        # folder_path = os.path.join(os.path.dirname(__file__), '..', 'data')  # Add your files here

        # Step 2: Preprocess Data
        documents = []
        for root, dirs, files in os.walk(self.DATA_DIR):
            for file in files:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    documents.append((f.read(), os.path.basename(f.name)))
        # print(documents)
        #3. Create Embeddings
        

        #4. Add Documents to Vector Store
        documents = [Document(id=documents[i][1], page_content=documents[i][0], metadata={"source": documents[i][1]}) for i in range(len(documents))]
        # documents = [Document(page_content=documents[i][0], metadata={"source": documents[i][1]}) for i in range(len(documents))]
        self.db.add_documents(documents)

        msg = "added file vector"
        return msg

    def clear_collections(self):
        ids = []

        for root, dirs, files in os.walk(self.DATA_DIR):
            for file in files:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    ids.append(os.path.basename(f.name))

        self.db.clear_vector_db(ids)
        msg = "Collection Deleted"
        return msg
