from typing import Callable
import matplotlib.pyplot as plt
import numpy as np


def plot(title:str, f: Callable[[float], float], a: float, b: float, n: int, x0: float, x1: float, filename: str):

    x = np.linspace(a, b, n)
    y = [f(i) for i in x]

    plt.title(title)
    plt.plot(x, y, label="f(x)")
    plt.grid(True)
    plt.plot(x0, f(x0), 'o', color='green', label="Miejsce zerowe znalezione metodą bisekcji")
    plt.plot(x1, f(x1), 'o', color='red', label="Miejsce zerowe znalezione metodą stycznych")
    
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.savefig(filename)