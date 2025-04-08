import numpy as np
import sys


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def readMatricesFromFile(filename) -> list[tuple[np.matrix, np.matrix]]:
    with open(filename, "r") as f:
        content = f.read().strip()
    entries = content.split("\n\n")
    matrices = []
    for entry in entries:
        lines = entry.strip().split("\n")
        if len(lines) >= 2:
            A = np.matrix(lines[0])
            b = np.matrix(lines[1]).transpose()
            matrices.append((A, b))
    return matrices


def isDiagonallyDominant(A: np.matrix) -> bool:
    abs_A = np.abs(A)
    # czy przekątna jest większa niż suma pozostałych elementów w wierszu
    #
    # jak sumujemy cały wiersz (razem z przekątną)
    # to musimy porównać z elementem przekątnej * 2
    # żeby sie zawierało
    #
    # x > [...]
    # dodajemy po obu stronach x
    # x+x > x+[...]
    # 2*x > [...]
    return np.all(2 * np.diag(abs_A) > np.sum(abs_A, axis=1))


def isContradictory(A: np.matrix, b: np.matrix) -> bool:
    macierz_rozszerzona = np.column_stack((A, b))

    rzad_A = np.linalg.matrix_rank(A)
    rzad_macierzy_rozszerzonej = np.linalg.matrix_rank(macierz_rozszerzona)

    if rzad_A < rzad_macierzy_rozszerzonej:
        return True

    if rzad_A == rzad_macierzy_rozszerzonej:
        if rzad_A < A.shape[1]:
            print("Układ nieoznaczony")  # nieskończenie wiele rozwiązań
        else:
            print("Układ oznaczony")  # jedno rozwiązanie
        return False

    return False


def jacobiMethod(
    A: np.matrix, b: np.matrix, x: np.matrix, epsilon: float, max_iterations: int
):
    diag = np.asmatrix(np.copy(np.diag(A))).transpose()
    np.fill_diagonal(A, 0)  # we dont want to sum diagonal elements
    for iteration in range(1, max_iterations + 1):
        multiplied = np.matmul(A, x)
        x_new = (b - multiplied) / diag
        print(x_new)
        max_diff = np.max(np.abs(x_new - x))
        x = x_new
        if max_diff < epsilon:
            print(
                f"{bcolors.OKGREEN}Zbieżność osiągnięta po {iteration} iteracjach.{bcolors.ENDC}"
            )
            return x
        print(f"Iteracja {iteration}: x = \n{x}\nRóżnica = {max_diff}\n")
    print(
        f"{bcolors.FAIL}Nie osiągnięto zbieżności w zadanej liczbie iteracji.{bcolors.ENDC}"
    )
    return x


def main():
    if len(sys.argv) < 2:
        print("Użycie: python main.py <nazwa_pliku>")
        sys.exit(1)
    filename = sys.argv[-1]
    matrices = readMatricesFromFile(filename)

    print(f"\nZnaleziono {len(matrices)} przykładów.")
    for i, (A, b) in enumerate(matrices):
        print(f"{i+1}: Układ {len(A)} równań")

    index = int(input("Wybierz numer przykładu do rozwiązania: ")) - 1
    A, b = matrices[index]

    print("\nWybrany układ równań:")
    print(f"{bcolors.OKBLUE}Macierz A:{bcolors.ENDC}")
    print(A)
    print(f"{bcolors.OKBLUE}Macierz b:{bcolors.ENDC}")
    print(b)

    if isContradictory(A, b):
        print(f"{bcolors.FAIL}Układ jest sprzeczny.{bcolors.ENDC}")
        return

    if not isDiagonallyDominant(A):
        print(
            f"{bcolors.WARNING}\nMacierz NIE jest dominująca diagonalnie. Metoda Jacobiego może się nie zbiegać.{bcolors.ENDC}"
        )

    x_init = np.matrix(np.zeros((len(A), 1)))
    print("\nPodaj wektor początkowy x0:")
    for i in range(len(A)):
        val = float(input(f"x[{i+1}] = "))
        x_init[i, 0] = val

    epsilon = float(input("Podaj dokładność (epsilon): "))
    max_iterations = int(input("Podaj maksymalną liczbę iteracji: "))

    result = jacobiMethod(A, b, x_init, epsilon, max_iterations)
    print("\nOstateczne przybliżone rozwiązanie:")
    for i, val in enumerate(result):
        print(f"x[{i+1}] = {val}")


if __name__ == "__main__":
    main()
