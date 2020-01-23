import random
#def doubleEven(num):
#     if num % 2 == 0:
#         num = num*2
#         return num
#     else:
#         num = -1
#         return num
# num = 10
# print(doubleEven(num))
# print(num)

# def grade(percent):
#     if percent <= 49:
#         letter = str("F")
#         return letter
#     elif percent >= 90:
#         letter = str("A")
#         return letter
#     elif percent >= 80:
#         letter = str("B")
#         return letter
#     elif percent >= 65:
#         letter = str("C")
#         return letter
#     elif percent >= 50:
#         letter = str("D")
#         return letter
# percent = int(input("What is your percent"))
# print(grade(percent))

# def largestNum(num1, num2, num3):
#     li = [num1, num2, num3]
#     return max(li)

# print(largestNum(6, 8, 5))
#
# def sumDice(Dice, numRolls):
#     sumdice = 0
#     for i in range(0, numRolls):
#         num = random.randint(1, Dice)
#         sumdice += num
#     return sumdice

# x = 1
# shoop_list = []
# while x == 1:
#     item = input("What do you want to purchase")
#     shoop_list.insert(0 ,item)
#     continue_shoop = int(input("Do you want to keep shopping, press 1 for yes and 2 for no"))
#     if continue_shoop == 1:
#         print("Your shopping list is", shoop_list)
#     elif continue_shoop == 2:
#         print("Your shopping list is", shoop_list, "thanks for shopping")
#         x = 0

# upper = 97
# def prime_nums():
#     for num in range(0, upper + 1):
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else:
#                 print(num)
# prime_nums()

# def diceRoll(rolls):
#     one = 0
#     two = 0
#     three = 0
#     four = 0
#     five = 0
#     six = 0
#     for i in range(0, rolls):
#         roll = random.randint(1, 6)
#         if roll == 1:
#             one += 1
#         elif roll == 2:
#             two += 1
#         elif roll == 3:
#             three += 1
#         elif roll == 4:
#             four += 1
#         elif roll == 5:
#             five += 1
#         elif roll == 6:
#             six += 1
#     print("one", one, "two", two, "three", three, "four", four, "five", five, "six", six)
# diceRoll(8)

# newList = []
# def pivotList(inList, num):
#     for i in range(len(inList)):
#         if inList[i] <= num:
#             newList.append(i)
#     return newList
# print(pivotList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

# def largestValue(inList):
#     highestNum = 0
#     for x in inList:
#         if x > highestNum:
#             highestNum = x
#     return highestNum
# print(largestValue([67374, 845346, 654, 1 , 2, 3, 574, 1046, 192, 420, 12]))

list1 = [3, 45, 86, 34, 21, 8]
list2 = [49, 76, 28, 0, 12, 23]
newList2 = []

def mergeList(list1, list2):
    bigList = list1 + list2
    minimum = bigList[0]
    sorting = True
    while sorting:
        for x in bigList:
            if x < minimum:
                minimum = x
        newList2.append(minimum)
        bigList.remove(minimum)
    return newList2
print(mergeList([3, 45, 86, 34, 21, 8], [49, 76, 28, 0, 12, 23]))
