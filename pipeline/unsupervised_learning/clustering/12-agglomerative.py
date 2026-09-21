#!/usr/bin/env python3
"""Module that performs agglomerative clustering on a dataset."""
import scipy.cluster.hierarchy
import matplotlib.pyplot as plt


def agglomerative(X, dist):
    """Perform agglomerative clustering with Ward linkage on a dataset.

    Displays the resulting dendrogram with each cluster shown in a
    different color.

    Args:
        X (numpy.ndarray): Dataset of shape (n, d).
        dist (float): Maximum cophenetic distance for all clusters.

    Returns:
        numpy.ndarray: Cluster indices of shape (n,) for each data point.
    """
    linkage = scipy.cluster.hierarchy.linkage(X, method='ward')
    clss = scipy.cluster.hierarchy.fcluster(
        linkage, t=dist, criterion='distance')
    scipy.cluster.hierarchy.dendrogram(linkage, color_threshold=dist)
    plt.show()
    return clss
