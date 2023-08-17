def sel_sort(listin):
    suffix_start = 0
    while suffix_start != len(listin):
        for i in range(suffix_start, len(listin)):
            if listin[i] < listin[suffix_start]:
                listin[suffix_start], listin[i] = listin[i], listin[suffix_start]
            print(f'i: {i}, list: {listin}')
        print(f'suffix_start: {suffix_start}')
        suffix_start += 1


list1 = [2, 3, 1]
sel_sort(list1)
