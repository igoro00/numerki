def horner(lista_wspolczynnikow: list[int], arg_x: float):
    """
    Zwracanie wartości wybranego wielomianu z użyciem schematu Hornera

    Parametry
    ----------
    lista_wspolczynnikow : list[int]
        wartości współczynników wielomianu zapisane w liście
        w kolejności od stojącego przy najwyższej potędze do wyrazu wolnego
    x : float
        argument dla którego obliczamy wartość funkcji
    
    Zwraca
    -------
    wynik : float
        wynik obliczeń
    """
    wynik = 0.0
    for item in reversed(lista_wspolczynnikow):    # pobiera współczynniki wielomianu od końca
        wynik = wynik * arg_x + item
    return wynik    # zwrot wartosci wielomianu