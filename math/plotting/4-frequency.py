#!/usr/bin/env python3
"""This module contains a function to plot a Matplotlib histogram."""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """
    plot a histogram of student scores for a project:
    The x-axis label is Grades
    The y-axis label is Number of Students
    The x-axis has bins every 10 units
    The title is Project A
    Bars are outlined in black
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    bins = np.arange(0, 101, 10)
    plt.hist(student_grades, bins=bins, edgecolor="black")
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.xlim(0, 100)
    plt.xticks(bins)

    plt.title("Project A")
    plt.show()
