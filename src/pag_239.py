def make_change(coin_vals, change):
    """
    coin_vals is a list of positive ints and coin_vals[0] =1
    change is a positive int,
    return the minimum number of coins needed to have a
    set of coins the values of which sum to change.
    Coins may be used more than once.
    For example, make_change([1, 5, 8], 11) should return 3.
    """

    # Basarlo en la división entera y en el módulo. Con la división entera == 0, sé si change es mayor que cada
    # número en la lista.
    # (1027//5)*5 + 1027%5 == 1027  TRUE.
