def fibonannci_gen(n):
    print(f'number computed: {n}')
    if n == 1 or n == 0:
        return 1
    else:
        return fibonannci_gen(n - 1) + fibonannci_gen(n - 2)


def factorial(nIn):
    if nIn == 0 or nIn == 1:
        return 1
    else:
        return nIn * factorial(nIn - 1)


def combinations(trials, successes):
    return factorial(trials) / (factorial(successes) * factorial(trials - successes))
