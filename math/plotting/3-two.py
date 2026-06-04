#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def two():
    """
    plot x ↦ y1 and x ↦ y2 as line graphs:
    The x-axis is labeled Time (years),
    The y-axis is labeled Fraction Remaining,
    The title is Exponential Decay of Radioactive Elements,
    The x-axis ranges from 0 to 20,000,
    The y-axis ranges from 0 to 1,
    x ↦ y1 is  plotted with a dashed red line,
    x ↦ y2 is be plotted with a solid green line,
    A legend labeling x ↦ y1 as C-14 and x ↦ y2 as Ra-226,
    is placed in the upper right hand corner of the plot.
    """
    x = np.arange(0, 21000, 1000)
    r = np.log(0.5)
    t1 = 5730
    t2 = 1600
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(x, y1, "--r", label="C14")
    plt.plot(x, y2, "-g", label="Ra-226")
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")
    plt.title("Exponential Decay of Radioactive Elements")
    plt.xlim(0, 20000)
    plt.ylim(0, 1)
    plt.legend(loc="upper right")
    plt.show()
