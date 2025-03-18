from typing import Callable


def stopCondition(
    y: float, iter: int, epsilon: float | None, max_iter: int | None
) -> bool:
    if y == 0:
        return True
    if max_iter is not None:
        if iter >= max_iter:
            return True
    if epsilon is not None:
        if abs(y) < epsilon:
            return True
    return False


def checkStartingCondition(
    f: Callable[[float], float],
    a: float,
    b: float,
    epsilon: float | None,
    max_iter: int | None,
) -> None:
    if epsilon is None and max_iter is None:
        raise ValueError("Musisz podać epsilon lub max_iter")
    if epsilon is not None and max_iter is not None:
        raise ValueError("Podaj tylko epsilon lub max_iter")
    if epsilon is not None and epsilon <= 0:
        raise ValueError("Epsilon musi być większy od zera")
    if max_iter is not None and max_iter <= 0:
        raise ValueError("max_iter musi być większy od zera")
    if a >= b:
        raise ValueError("a musi być mniejsze od b")
    if f(a) * f(b) > 0:
        raise ValueError("f(a) i f(b) muszą mieć różne znaki")
    return