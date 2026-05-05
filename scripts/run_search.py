from src.preprocessing import load_and_clean_docs
from src.chunking import chunking
from src.embeddings import make_embeddings, load_embeddings
from src.search import search
from src.utils import print_results
import os

EMBEDDINGS_FILE = "data/processed/embeddings.pickle"

query = "In The Strange Case of Dr. Jekyll and Mr. Hyde, what is the name of the lawyer who investigates Jekyll's situation?"

queries = [
    "In Alice''s Adventures in Wonderland, what does Alice drink or eat that causes her to change size?",
    "In Romeo and Juliet, what is the name of Juliet's nurse?",
    "In The Great Gatsby, who hosts the parties at the Gatsby mansion?",
    "In A Room with a View, in which country does Lucy Honeychurch travel during the story?"
]

if not os.path.exists(EMBEDDINGS_FILE):
    print('Gerando embeddings...')
    docs = load_and_clean_docs(folder_path='data/raw/')
    chunks = chunking(documents=docs)
    embeddings, vectors = make_embeddings(chunks=chunks)
else:
    print('Carregando embeddings')
    embeddings, vectors = (load_embeddings('embeddings.pickle'))

results = search(embeddings, vectors, queries)
print_results(results)