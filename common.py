list1 = [1,2,3]
list2 = [3,5,6]
common = []
for item in list1:
    if item in list2:
        common.append(item)

print(common)