def recursive_clustering(embeddings, model, depth=3, n_components=5):
    if depth == 0 or len(embeddings) <= 1:
        return embeddings

    cluster_labels, gmm = cluster_embeddings(embeddings, n_components=n_components)
    cluster_texts = {i: [] for i in range(n_components)}

    for idx, label in enumerate(cluster_labels):
        cluster_texts[label].append(embeddings[idx])

    summarized_texts = {}
    for label, texts in cluster_texts.items():
        if len(texts) > 0:
            summarized_text = summarize_texts([" ".join(text) for text in texts])
            summarized_texts[label] = summarized_text

    reembedded_texts = {label: reembed_texts(summ_texts, model) for label, summ_texts in summarized_texts.items()}

    new_embeddings = []
    for label, reembeds in reembedded_texts.items():
        new_embeddings.extend(recursive_clustering(reembeds, model, depth=depth-1, n_components=n_components))

    return new_embeddings

final_embeddings = recursive_clustering(summary_embeddings, model)