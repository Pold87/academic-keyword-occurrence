import matplotlib.pyplot as plt
import random


def test():
    years = list(range(2001, 2022 + 1))
    content = [random.randint(10, 10000) for i in range(len(years))]
    plot_bar("test", years, content)


def plot_bar(keyword, years, results):
    plt.figure(figsize=(10, 5))
    plt.bar(years, results, width=0.3, color="black", align="center")
    plt.title(f"Occurences of keyword {keyword} over time")
    plt.ylabel("Occurences")
    plt.xlabel("Year")
    plt.xticks(years, rotation=45)
    plt.tight_layout()


if __name__ == '__main__':
    test()
