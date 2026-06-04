#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """
    Plot x ↦ y as a scatter plot:
    The x-axis is labeled Height (in)
    The y-axis is labeled Weight (lbs)
    The title is Men's Height vs Weight
    Datapoints are plotted as magenta dots
    """
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180
    plt.figure(figsize=(6.4, 4.8))
    plt.plot(x, y, "om")
    plt.xlabel("Height (in)")
    plt.ylabel("Weight (lbs)")
    plt.title("Men's Height vs Weight")
