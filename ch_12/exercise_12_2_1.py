import figure_12_5 as merge

sorted_tuples = merge.merge_sort([(0, 5), (2, 4), (3, 3)], compare=lambda x, y: sum(x) < sum(y))
print(sorted_tuples)
sorted_tuples_2 = sorted([(0, 5), (2, 4), (3, 3)], key=max)
print(sorted_tuples_2)
