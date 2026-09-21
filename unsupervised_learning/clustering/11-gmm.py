#!/usr/bin/env python3
"""Module that calculates a GMM from a dataset using scikit-learn."""
import sklearn.mixture


def gmm(X, k):
    """Calculate a Gaussian Mixture Model from a dataset using scikit-learn.

    Args:
        X (numpy.ndarray): Dataset of shape (n, d).
        k (int): Number of clusters.

    Returns:
        tuple: (pi, m, S, clss, bic)
            pi (numpy.ndarray): Cluster priors of shape (k,).
            m (numpy.ndarray): Centroid means of shape (k, d).
            S (numpy.ndarray): Covariance matrices of shape (k, d, d).
            clss (numpy.ndarray): Cluster indices of shape (n,).
            bic (float): BIC value of the model.
    """
    model = sklearn.mixture.GaussianMixture(n_components=k)
    model.fit(X)
    clss = model.predict(X)
    bic = model.bic(X)
    return model.weights_, model.means_, model.covariances_, clss, bic
