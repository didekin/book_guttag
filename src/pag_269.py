def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(listin, compare=lambda x, y: x < y):
    print(f'listinIn = {listin}')
    if len(listin) < 2:
        return listin[:]
    else:
        middle = len(listin) // 2
        left = merge_sort(listin[:middle], compare)
        right = merge_sort(listin[middle:], compare)
        print(f'left = {left}, right = {right}')
        merge_rec = merge(left, right, compare)
        print(f'merge_rec = {merge_rec}')
        return merge_rec


intList = [(1, 2), (1, 0, 1), (2, 0, 0, 5), (1, 1, 1, 2, 3)]
sort_intlist = merge_sort(intList, lambda x, y: sum(x) < sum(y))
print(sort_intlist)
