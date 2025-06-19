def find_an_even(L):
    """Assumes L is a list of integers
       Returns the first even number in L
       Raises ValueError if L does not contain an even number"""
    even_num = 0
    for num in L:
        if num % 2 == 0:
            even_num = num
            break
        raise ValueError(' L does not contain an even number')
    return even_num

