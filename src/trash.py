list1 = ['a','b']
list1.append('c')
temp = list1[:]
temp.reverse()
print(list1)
print(temp)
print(list1 == temp)