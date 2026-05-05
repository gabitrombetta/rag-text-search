import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize

from embeddings import embedding_model

def search(embeddings:list, chunk_vectors:np.ndarray, query:str | list, top_k:int=10, score_threshold:float=0.3) -> list:
    queries = [query] if isinstance(query, str) else query

    query_vectors = normalize([embedding_model.embed_query(q) for q in queries])

    all_results = []

    for query_idx, query_vec in enumerate(query_vectors):
        similarity_scores = cosine_similarity([query_vec], chunk_vectors)[0]

        ranked_indices = np.argsort(-similarity_scores)

        results = []
        seen_ids = set()

        for i in ranked_indices:
            if embeddings[i]['id'] in seen_ids:
                continue

            score = float(similarity_scores[i])

            if score < score_threshold:
                continue

            seen_ids.add(embeddings[i]['id'])

            results.append({
                'query': queries[query_idx],
                'text': embeddings[i]['text'][:300] + "...",
                'document': embeddings[i]['document'],
                'score': round(score, 4)
            })

            if len(results) == top_k:
                break

        all_results.append(results)

    return all_results