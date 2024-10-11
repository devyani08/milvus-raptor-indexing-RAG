from rank_bm25 import BM25Okapi
import numpy as np

def hybrid_search(query, collection, top_k=5):
    # Query expansion (simple example, can be expanded)
    expanded_query = query + " " + " ".join(synonyms(query))
    
    # BM25 search
    tokenized_corpus = [doc.split() for doc in chunks]
    bm25 = BM25Okapi(tokenized_corpus)
    bm25_scores = bm25.get_scores(expanded_query.split())
    
    # Dense retrieval
    query_embedding = model.encode([expanded_query])[0]
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}, "offset": 0}
    results = collection.search(
        data=[query_embedding],
        anns_field="embedding",
        param=search_params,
        limit=top_k,
        output_fields=["text", "metadata"]
    )
    
    # Combine and re-rank results
    combined_results = []
    for i, hit in enumerate(results[0]):
        bm25_score = bm25_scores[hit.id]
        dense_score = 1 / (1 + hit.distance)  # Convert distance to similarity
        combined_score = 0.5 * bm25_score + 0.5 * dense_score
        combined_results.append((hit.entity.get('text'), hit.entity.get('metadata'), combined_score))
    
    # Sort by combined score
    combined_results.sort(key=lambda x: x[2], reverse=True)
    return combined_results[:top_k]

# Example usage
search_results = hybrid_search("What is the capital of France?", collection)
for text, metadata, score in search_results:
    print(f"Score: {score:.4f}")
    print(f"Text: {text[:100]}...")
    print(f"Metadata: {metadata}")
    print()