import chromadb
from chromadb.utils import embedding_functions

# Initialize the Chroma client (persists data to a local folder)
client = chromadb.PersistentClient(path="./chroma_db")

# Use a default embedding function (sentence-transformers)
# This model converts your text into vectors automatically
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Create or get a collection (like a table in SQL)
collection = client.get_or_create_collection(
    name="student_alumni_data", 
    embedding_function=embedding_func
)

def add_to_vector_db(id, text, metadata):
    """Add a document (e.g., student profile or alumni bio) to the vector DB"""
    collection.add(
        ids=[str(id)],
        documents=[text],
        metadatas=[metadata]
    )

def query_vector_db(query_text, n_results=5):
    """Search for the most similar records"""
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
    return results