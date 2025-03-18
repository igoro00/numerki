from bisekcja import bisekcja
from funkcje import I_Funkcja, funkcje
import questionary

from plot import plot
from styczne import styczne


def main():

    res = questionary.select(
        "Wybierz funkcję do zbadania:",
        choices=[f["name"] + ": " + f["wzor"] for f in funkcje],
    ).ask()
    a = 0
    b = 0
    selected_func = next(f for f in funkcje if f["name"] + ": " + f["wzor"] == res)
    while True:
        a = float(questionary.text(message="Podaj a:").ask())
        b = float(questionary.text(message="Podaj b:").ask())
        if selected_func["f"](a) * selected_func["f"](b) < 0:
            break
        print("f(a) i f(b) muszą mieć różne znaki")

    stopCondition = questionary.select(
        "Wybierz kryterium zatrzymania:", choices=["Dokładność", "Ilość iteracji"]
    ).ask()
    epsilon = None
    max_iter = None
    if stopCondition == "Dokładność":
        epsilon = float(questionary.text("Podaj dokładność:").ask())
    else:
        max_iter = int(questionary.text("Podaj ilość iteracji:").ask())

    print("Obliczanie metodą bisekcji")
    (b_wynik, b_iter) = bisekcja(
        selected_func["f"], a=a, b=b, epsilon=epsilon, max_iter=max_iter
    )
    print(
        f"Wynik metody bisekcji: f({round(b_wynik,4)})={round(selected_func["f"](b_wynik),6)}"
    )
    print(f"Ilość iteracji: {b_iter}")
    print()
    print("Obliczanie metodą stycznych")
    (s_wynik, s_iter) = styczne(
        selected_func["f"], selected_func["d"], a, b, epsilon, max_iter
    )
    print(
        f"Wynik metody stycznych: f({round(s_wynik,4)})={round(selected_func["f"](s_wynik),6)}"
    )
    print(f"Ilość iteracji: {s_iter}")
    print("\n")

    stopText = ""
    if(epsilon is not None):
        stopText = f"ε = {epsilon}"
    else:
        stopText = f"max_iter = {max_iter}"
    plot(
        f"f. {selected_func['name']}: {selected_func['wzor']}, {stopText}",
        selected_func["f"],
        a,
        b,
        1000,
        b_wynik,
        s_wynik,
        selected_func["name"]+"_"+stopCondition+".png",
    )


if __name__ == "__main__":
    main()
