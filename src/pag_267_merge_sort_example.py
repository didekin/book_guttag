def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append([left[i]])
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
    if len(listin) < 2:
        return listin[:]
    else:
        middle = len(listin) // 2
        left = merge_sort(listin[:middle], compare)
        right = merge_sort(listin[middle:], compare)
        return merge(left, right, compare)
