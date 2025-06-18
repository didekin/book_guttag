def is_pal(x):
    """Assumes x is a list
        Returns True if the list is a palindrome; False
otherwise"""
    temp = x
    x.reverse()
    print(x)
    print(temp)
    return temp == x


pal = is_pal(['a', 'b'])
print(pal)