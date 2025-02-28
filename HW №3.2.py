# list1 = [1, 5, 7, 66, 3, 8, 9, 111]
# list2 = [1,5,6,10,44]
# list3 = [1, ]
# list4 = []
#
# list5 = [list1[slice(len(list1)//2)], list1[slice(len(list1)//2, len(list1))]]
#
# list6 = [list2[slice(len(list2) // 2)], list2[len(list2) // 2:]]
#
# list7 = [list3[len(list3) // 2:] , list3[slice(len(list3) // 2)]]
#
# list8 = [list4[len(list4) // 2:] , list4[slice(len(list4) // 2)]]
#
# print(list5)
# print(list6)
# print(list7)
# print(list8)


list1 = [1, 5, 7, 66, 3, 8, 9, 111]
list2 = [1,5,6,10,44]
list3 = [1, ]
list4 = []

list5 = [list1[:len(list1)//2] , list1[len(list1)//2:]]

list6 = [list2[:len(list2)//2] , list2[len(list2)//2:]]

list7 = [list3[len(list3)//2:] , list3[:len(list3)//2]]

list8 = [list4[:len(list4)//2] , list4[len(list4)//2:]]

print(list5)
print(list6)
print(list7)
print(list8)