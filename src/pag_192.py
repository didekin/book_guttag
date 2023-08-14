def sum_digits(s):
    """Assumes s is a string
       Returns the sum of the decimal digits in s
       For example, if s is 'a2b3c' it returns 5"""
    nums = []
    for c in s:
        if c.isdecimal():
            nums.append(int(c))
    return sum(nums)


print(sum_digits('ab'))
