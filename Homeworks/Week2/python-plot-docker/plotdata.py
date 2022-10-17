import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
import matplotlib.dates as mdates


data = pd.read_csv("./data/coding-environment-exercise.csv", index_col=0, header=0)

def main():
    x = data.index
    y = data['value']

    fig, ax = plt.subplots()
    plt.plot(x, y, marker='.', color='black', markersize=8)
    plt.xticks(x, data.index, rotation=90)
    plt.title("Coding environment exercise - Plot")
    plt.ylabel('value')
    plt.xlabel('date')
    plt.tight_layout()

    plt.savefig("plot.png", bbox_inches='tight')
    plt.show()

    print("Done")


if __name__ == '__main__':
    main()