def reembed_texts(texts, model):
    return model.encode(texts)

# Assuming `model` is the SentenceTransformer model from previous steps
summary_texts = [" ".join(summaries) for summaries in cluster_summaries.values()]
summary_embeddings = reembed_texts(summary_texts, model)