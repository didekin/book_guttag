from argparse import ArgumentParser


def fibonacci_iter(n):
    if n <= 1:
        return n
    f2, f1 = 0, 1
    for i in range(2, n + 1):
        f2, f1 = f1, f1 + f2
    return f1


parser = ArgumentParser()
parser.add_argument(dest='intnumber', type=int)
args_in = parser.parse_args()
numarg = args_in.intnumber

print(fibonacci_iter(numarg))

# Call in the terminal python3 src/fibonacci_iterative.py 10
# And get: 55.
