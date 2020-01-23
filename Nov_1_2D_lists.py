# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]
#
# newlist = [a, b, c]
# for i in range(len(newlist)):
#     print(newlist[i][2])
#
# for x in newlist[0]:
#     print(x)
#
# newlist2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
# print(newlist2[1][1])
#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = [list1, list2]
# for i in list3:
#     for x in i:
#         print(x)


list4 = input("What row do you want to sum")
list5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0
for i in list5[list4]:
    sum = sum +i
    print(sum)

list6 = input("What column do you want to sum")
list7 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in list6:
    if list6 == 1:
        print(list5[1])
    elif list6 == 2:
        print(list5[2])
    elif list6 == 0:
        print(list5[0])