def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def listfibo(numitems):
    fibos = []
    for i in range(numitems):
        fibos.append(fibo(i))
    return fibos


with open('files/fib_file', 'w') as fibohandle:
    for k in map(str, listfibo(10)):
        fibohandle.writelines(k + '\n')


with open('files/fib_file', 'r') as fibohandle:
    for line in fibohandle:
        print(line[:-1])

