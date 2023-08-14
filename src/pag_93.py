def find_root(x, power, epsilon):
    # check even powerand x negative
    if x < 0 and power % 2 == 0:
        return None
    low = min(-1, x)
    high = max(1, x)
    ans = (low + high) / 2
    while abs(pow(ans, power) - x) > epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (low + high) / 2
    return ans


def is_in(s1, s2):
    return s1 in s2 or s2 in s1


def test_is_in(arr_s1, arr_s2):
    for s11 in arr_s1:
        for s22 in arr_s2:
            res = is_in(s11, s22)
            if res != (s11 in s22 or s22 in s11):
                print('FAIL')
    for s22 in arr_s2:
        for s11 in arr_s1:
            res = is_in(s22, s11)
            if res != (s22 in s11 or s11 in s22):
                print('FAIL')


# epsi = 0.001
# sumpowers = find_root(25, 2, epsi) + find_root(-8, 3, epsi) + find_root(16, 4, epsi)
# print(sumpowers)
#
# print(is_in('hola pedro', 'hola'))
# print(is_in('pedro', 'hola'))

arr1 = ('hola', 'adios', 'si', 'no')
arr2 = ('la', 'dios', 'sin', 'non')
test_is_in(arr1,arr2)
