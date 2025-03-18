from typing import Callable

from utils import checkStartingCondition, stopCondition


def styczne(
    f: Callable[[float], float], 
    d:Callable[[float], float], 
    a: float, b: float, 
    epsilon: float|None, 
    max_iter: int|None
) -> tuple[float, int]:
    checkStartingCondition(f, a, b, epsilon, max_iter)
    x=b
    iter = 0
    while stopCondition(abs(f(x)), iter, epsilon, max_iter) == False:
        iter+=1
        x = x - f(x) / d(x)
    return x, iter