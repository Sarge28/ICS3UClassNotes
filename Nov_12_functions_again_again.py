# import random
# import time
#
# def isOddorEven(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# if isOddorEven(5) == "Even":
#     print("You typed a  even number")
# else:
#     print("You typed a odd number")
#
# def time_random():
#     num_boo = random.randint(1,5)
#     time.sleep(num_boo)
#     print("BOO!")
# time_random()
#
# def back_num(num):
#     num = str(num)
#     num = num[::-1]
#     print(num)
# num = int(input("Type a number"))
# back_num(num)
#
def winter(snow):
    if snow >= 10:
        return "True"
    elif snow <= 5:
        return "False"
    else:
        return "Maybe"
snowfall = int(input("How much snow will fall tonight in centimeters?"))
if winter(snowfall) == "False":
    print("It will snow less than 5 centimeters")
elif winter(snowfall) == "True":
    print("It will snow more than 10 centimeters")
else:
    print("It will snow between 5 and 10 centimeters")
