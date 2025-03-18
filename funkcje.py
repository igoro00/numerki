from typing import Callable, TypedDict
import math

class I_Funkcja(TypedDict):
    name: str
    f: Callable[[float], float]
    d: Callable[[float], float]
    wzor: str

funkcje: list[I_Funkcja] = [
    {
        "name": "wielomianowa",
        "f": lambda x: 2*(x**2) + x - 4,
        "d": lambda x: 4*x + 1,
        "wzor": "2x^2 + x - 4"
    },
    {
        "name": "trygonometryczna",
        "f": lambda x: math.tan(x/2)-1,
        "d": lambda x: 1/(2*(math.cos(x/2)**2)),
        "wzor": "tan(x/2) - 1",
    },
    {
        "name": "wykladnicza",
        "f": lambda x: math.exp(x+1) - math.pi,
        "d": lambda x: math.exp(x+1),
        "wzor": "e^(x+1) - pi",
    },
    {
        "name": "złożona",
        "f": lambda x: math.sin((x**2)-9*x) + math.exp(x),
        "d": lambda x: (2*x - 9)*math.cos((x**2)-9*x) + math.exp(x),
        "wzor": "sin(x^2 - 9x) + e^x"
    }
]