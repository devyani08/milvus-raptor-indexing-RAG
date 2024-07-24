import numpy as np
from sklearn.mixture import GaussianMixture
all_embeddings = np.vstack([embeddings1, embeddings2, embeddings3])


def cluster_embeddings(embeddings, n_components=5):
    # Reshape embeddings to 2D if it's 1D
    if embeddings.ndim == 1:
        embeddings = embeddings.reshape(-1, 1)  # Reshape to a column vector

    gmm = GaussianMixture(n_components=n_components, covariance_type='full')
    gmm.fit(embeddings)
    cluster_labels = gmm.predict(embeddings)
    return cluster_labels, gmm

cluster_labels, gmm = cluster_embeddings(all_embeddings)