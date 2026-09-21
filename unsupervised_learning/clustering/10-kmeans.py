#!/usr/bin/env python3
"""Module that performs K-means clustering using scikit-learn."""
import sklearn.cluster


def kmeans(X, k):
    """Perform K-means clustering on a dataset using scikit-learn.

    Args:
        X (numpy.ndarray): Dataset of shape (n, d).
        k (int): Number of clusters.

    Returns:
        tuple: (C, clss)
            C (numpy.ndarray): Centroid means of shape (k, d).
            clss (numpy.ndarray): Cluster indices of shape (n,).
    """
    model = sklearn.cluster.KMeans(n_clusters=k)
    model.fit(X)
    return model.cluster_centers_, model.labels_
