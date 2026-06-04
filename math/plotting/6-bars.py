import numpy as np
import matplotlib.pyplot as plt


def bars():
    """
    Plots a stacked bar graph:
    The title is Number of Fruit per Person,
    The y-axis label is Quantity of Fruit,
    The legend indicates one color per fruit type,
    Each person gets a stacked bar (3 total),
    Each stacked bar represents the fruit count posessed by each person,
    The stack order from bottom to top is always: apples in red,
    bananas in yellow, oranges in orange, peaches in peach colors.
    """
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    people = ["Farrah", "Fred", "Felicia"]
    fruits = ["apples", "bananas", "oranges", "peaches"]
    colors = ["red", "yellow", "#ff8000", "#ffe5b4"]
    x = np.arange(len(people))
    bottoms = np.zeros(len(people))
    for i in range(len(fruits)):
        plt.bar(
            x,
            fruit[i],
            width=0.5,
            bottom=bottoms,
            color=colors[i],
            label=fruits[i]
        )
        bottoms += fruit[i]
    plt.xticks(x, people)
    plt.ylabel("Quantity of Fruit")
    plt.yticks(np.arange(0, 81, 10))
    plt.ylim(0, 80)
    plt.title("Number of Fruit per Person")
    plt.legend()
    plt.show()
