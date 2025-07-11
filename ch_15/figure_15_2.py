def fib_memo(n, memo=None):
    """Assumes n is an int >= 0, memo used only by recursive calls
    Returns Fibonacci of n"""
    if memo is None:
        memo = {}
    if n == 0 or n == 1:
        return 1
    try:
        print(f'memo try = {memo}')
        return memo[n]
    except KeyError:
        result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        print(f'result except = {result}')
        memo[n] = result
        print(f'memo except = {memo}')
        return result


def fib_tab(n):
    """Assumes n is an int > 0
    Returns Fibonacci of n"""
    tab = [1] * (n + 1)  # n+1 because first two values matter
    print(f'tab-0: {tab}')
    for i in range(2, n + 1):
        tab[i] = tab[i - 1] + tab[i - 2]
        print(f'tab-{i}: {tab}')
    print(f'tab-final:{tab}')
    return tab[n]


# print(fib_memo(2))
# print(fib_memo(3))
print(fib_memo(120))
