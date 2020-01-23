import random
# temp_list = [6,  3, 4, 2, 10]
# for i in range(len(temp_list)):
#     print(temp_list[i])
#
# temp_list2 = [6, 3, 4, 2, 10]
# for i in range(len(temp_list2)):
#     temp_list2[i] = 10 + i
#     print(temp_list2[i])
#
# temp_list3 = [2, 5, 3, 8, 1, 10, 7, 9, 4, 6]
# for i in range(len(temp_list3)):
#     temp_list3.sort(reverse=False)
#     print(temp_list3[i])
#
# temp_list4 = [1, 2, 3, 4, 5]
# temp_list4_5 = [6, 7, 8, 9, 10]
# for i in range(0, 2):
#     print(max(temp_list4))
#     temp_list4 = temp_list4_5
#
# temp_list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(temp_list5)):
#     print(temp_list5[i])
#
# temp_list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(temp_list5)):
#     if i % 2 == 1:
#         print(temp_list5[i])
#
# names = ["Sarge", "Espy", "Jimmy"]
# for name in names:
#     print(name)
#
# weekdays = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri"]
# for weekday in weekdays:
#     print(weekday)
# del weekdays[0]
# for weekday in weekdays:
#     print(weekday)
# weekdays = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri"]
# for weekday in weekdays:
#     print(weekday)
# weekdays.remove("Sun")
# for weekday in weekdays:
#     print(weekday)
#
# fruits = ["Banana", "Apple", "Kiwi", "Mango", "Peach"]
# for fruit in fruits:
#     print(fruit)
# del fruits[2]
# for fruit in fruits:
#     print(fruit)
#
# num = []
# num_length = random.randint(5, 10)
# for i in range(num_length):
#     num.append(i)
# if len(num) % 2 ==  0:
#     num.insert(0, "Even")
# else:
#     num.insert(0, "Odd")
# print(num)
#
# words = input("Type a word")
# for i in range(len(words)):
#     print(words[i])

harry = ["You’re a wizard Harry."]
print(harry)
harry = [i.replace("e", "3") for i in harry]
harry = [i.replace("o", "0") for i in harry]
harry = [i.replace("H", "4") for i in harry]
print(harry)

backword = input("Type a word")
backword(reverse=True)
reversed(backword)

