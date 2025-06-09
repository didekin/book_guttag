# Write a function is_in that accepts two strings as arguments and returns True if either string occurs anywhere in
# the other, and False otherwise. Hint: you might want to use the built-in str operator in.


def is_in(str1, str2):
    is_in_bool = False
    if str1 in str2 or str2 in str1:
        is_in_bool = True
    return is_in_bool


# Write a function to test is_in.

def test_is_in(str1, str2):
    result = is_in(str1, str2)
    print(f'{str1}, {str2}, {result}')


test_is_in('abc', 'bcd')
test_is_in('abc', 'bc')
test_is_in('abc', 'abcd')
test_is_in('abc', 'abc')
test_is_in('abc', 'cba')
