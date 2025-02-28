list1 = [1, 2, 3, 4]
if len(list1) >= 1:
    last_element = list1[-1]
    list1.insert(0, last_element)
    del list1[-1]
print(list1)