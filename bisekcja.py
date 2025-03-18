from typing import Callable

from utils import checkStartingCondition, stopCondition


def bisekcja(
    f: Callable[[float], float],
    a: float,
    b: float,
    epsilon: float | None,
    max_iter: int | None,
) -> tuple[float, int]:
    checkStartingCondition(f, a, b, epsilon, max_iter)
    iter = 1
    x = (a + b) / 2
    while stopCondition(abs(f(x)), iter, epsilon, max_iter) == False:
        iter += 1
        x = (a + b) / 2
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
    return (x, iter)
