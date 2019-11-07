# #  Task 1
# def math(num1, num2):
#     num3 = num1 * num2
#     return num3
# num1 = int(input("Pick a number?"))
# num2 = int(input("Pick a number?"))
# print(math(num1, num2))
#
# #  Task 2
# def inputT(str1, str2):
#     if str1 == str2:
#         return "True"
#     elif str1 != str2:
#         return "False"
#     return str1, str2
# str1 = input("Write a word?")
# str2 = input("Write a word?")
# inputT(str1, str2)
#
# #  Task 3
# def word_find(string, letter):
#     if letter in string:
#         return "True"
#     elif letter not in string:
#         return "False"
#     return string, letter
# string = input("Write a word?")
# string = string.lower()
# letter = input("Write a letter")
# letter = letter.lower()
# word_find(string, letter)
#
# #  Task 4
# import random
# def greetings():
#     greet_list = ["Hello there", "Bonjour", "Sup bro", "What's up dawg", "Dear wonderful person"]
#     greet = random.choice(greet_list)
#     return greet
#
# print(greetings())