# Clustering

This project covers unsupervised clustering algorithms, beginning with K-means clustering, evaluation techniques, and Gaussian Mixture Models.

## Requirements

- **Environment**: Ubuntu 20.04 LTS with Python 3.9
- **Libraries**:
  - `numpy` (version 1.25.2)
  - `scikit-learn` (version 1.5.0)
  - `scipy` (version 1.11.4)
- **Style**: `pycodestyle` (version 2.11.1)
- **Editors**: `vi`, `vim`, `emacs`
- All files must be executable and start with `#!/usr/bin/env python3`
- All modules, classes, and functions must have documentation

## Tasks

| File | Description |
| --- | --- |
| [0-initialize.py](./0-initialize.py) | Initializes cluster centroids for K-means using a multivariate uniform distribution |
| [1-kmeans.py](./1-kmeans.py) | Performs K-means clustering on a dataset |
| [2-variance.py](./2-variance.py) | Calculates the total intra-cluster variance for a dataset |
| [3-optimum.py](./3-optimum.py) | Finds the optimum number of K-means clusters by variance (elbow method) |
| [4-initialize.py](./4-initialize.py) | Initializes priors, centroids, and covariance matrices for a GMM |
| [5-pdf.py](./5-pdf.py) | Calculates the probability density function of a Gaussian distribution |
| [6-expectation.py](./6-expectation.py) | Calculates the E-step (posterior probabilities and log likelihood) for a GMM |
| [7-maximization.py](./7-maximization.py) | Calculates the M-step (updated priors, means, covariances) for a GMM |
| [8-EM.py](./8-EM.py) | Performs the full EM algorithm for a GMM with early stopping and verbose logging |
| [9-BIC.py](./9-BIC.py) | Finds the optimal number of GMM clusters using the Bayesian Information Criterion |
| [10-kmeans.py](./10-kmeans.py) | Performs K-means clustering on a dataset using scikit-learn |
| [11-gmm.py](./11-gmm.py) | Calculates a Gaussian Mixture Model from a dataset using scikit-learn |
| [12-agglomerative.py](./12-agglomerative.py) | Performs agglomerative clustering with Ward linkage and displays the dendrogram |
