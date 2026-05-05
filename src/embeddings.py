import pickle
from langchain_community.embeddings import HuggingFaceEmbeddings
from sklearn.preprocessing import normalize

EMBEDDING_MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'
EMBEDDINGS_FILE = 'embeddings.pickle'

embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

def make_embeddings(chunks: list, output_file=EMBEDDINGS_FILE) -> list:
    texts = [c['text'] for c in chunks]

    vectors = embedding_model.embed_documents(texts)

    for i, vec in enumerate(vectors):
        chunks[i]['embedding'] = vec

    with open(output_file, 'wb') as f:
        pickle.dump(chunks, f)

    normalized_vectors = normalize(vectors)

    return chunks, normalized_vectors

def load_embeddings(file: str) -> list:
    with open(file, 'rb') as f:
        chunks = pickle.load(f)

    vectors = [c['embedding'] for c in chunks]
    normalized_vectors = normalize(vectors)

    return chunks, normalized_vectors
