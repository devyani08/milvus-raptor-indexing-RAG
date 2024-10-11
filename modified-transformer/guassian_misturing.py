from sklearn.mixture import GaussianMixture

def cluster_embeddings(embeddings, n_clusters=10):
    gmm = GaussianMixture(n_components=n_clusters, random_state=42)
    cluster_probs = gmm.fit_predict(embeddings)
    return cluster_probs

# Example usage
cluster_assignments = cluster_embeddings(embeddings)
print(f"Assigned {len(cluster_assignments)} chunks to clusters")