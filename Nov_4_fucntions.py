import random

# def hello_world():
#     print("Hello World!")
#
# for x in range(0,5):
#     hello_world()
#
#
# def word(data):
#     word_thing = data.upper()
#     return word_thing
#
# print(word("banana"))
#
# def lottery():
#     num1 = random.randint(0, 9)
#     num2 = random.randint(0, 9)
#     num3 = random.randint(0, 9)
#     if num1 == num2 == num3:
#         print("You won the lottery")
#     print(num1, num2, num3)
# lottery()

def task_5(li, num):
    i = 0
    while len(li) > i: #for i in range(len(li)):
        if li[i] > num:
            del li[i]
            i = i-1
        i = i+1
    return li

ex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(task_5(ex_list, 4))

#
# list1 = []
# for i in range(0,3):
#     variable = int(input("Give me a number"))
#     list1.append(variable)
# print(list1)
