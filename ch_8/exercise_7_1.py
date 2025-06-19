def sum_digits(s):
    """Assumes s is a string.
    Returns the sum of the decimal digits in s.
    For example, if s is 'a2b3c' it returns 5"""
    nums = []
    for i in range(0, len(s)):
        if s[i].isdecimal():
            nums.append(int(s[i]))
    return sum(nums)


ss_1 = '-1a2'
ss_2 = ''
ss_3 = 'ab'
print(f'f: {sum_digits(ss_1)}, {sum_digits(ss_2)}, {sum_digits(ss_3)}')
