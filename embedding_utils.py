from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Initialize the Sentence-Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text_chunks):
    """
    Generate embeddings for the text chunks.
    """
    return model.encode(text_chunks)

def create_faiss_index(embeddings):
    """
    Create a FAISS index from the embeddings.
    """
    dimension = embeddings.shape[1]  # Get the dimension of embeddings
    index = faiss.IndexFlatL2(dimension)  # Use L2 distance metric
    index.add(embeddings)  # Add embeddings to the index
    return index

def get_answer(query, faiss_index, text_chunks):
    """
    Get the most relevant answer based on the query by searching the FAISS index.
    """
    query_embedding = model.encode([query])  # Generate query embedding
    _, indices = faiss_index.search(query_embedding, k=1)  # Search for the closest match
    
    # Return the chunk that corresponds to the closest match
    return text_chunks[indices[0][0]]
