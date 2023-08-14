def f(l1, l2):
    """L1, L2 lists of same length of numbers
    returns the sum of raising each element in L1
    to the power of the element at the same index in L2
    For example, f([1,2], [2,3]) returns 9"""
    sumout = 0
    for i in map(lambda x, y: x ** y, l1, l2):
        sumout += i
    return sumout


print(f([2, 3, 5], [1, 2, 3]))
