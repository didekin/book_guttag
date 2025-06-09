def find_last(s, sub):
    """s and sub are non-empty strings
       Returns the index of the last occurrence of sub in s.
       Returns None if sub does not occur in s"""
    if sub not in s:
        return None
    else:
        return s.rfind(sub)


print(find_last('abcabc', 'bc'))
print(find_last('abcabc', 'ef'))
