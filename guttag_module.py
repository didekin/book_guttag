def fibonannci_gen(n):
    print(f'number computed: {n}')
    if n == 1 or n == 0:
        return 1
    else:
        return fibonannci_gen(n - 1) + fibonannci_gen(n - 2)

