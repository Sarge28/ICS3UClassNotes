import math  # this is for the square root in the pythagoras part

# 1 Radar Technology

# speed = int(input("What is your speed in kilometers (don't add the sign)") # this makes it so the input is an integer
# if speed <= 20: #this code runs if the integer is less than 20
#     print("You are going to slow, speed up")
# elif speed <= 50: # this code runs if the integer is less than 50
#     print("You are going at a perfect speed")
# elif speed >= 81: # this code runs if the integer is greater than 81
#     print("You are going way too fast you will get a fine of $150!")
# elif speed >= 71: # this code runs if the integer is greater than 71
#     print("You are going too fast you will get a fine of $75!")
# elif speed >= 51: # this code runs if the integer is greater than 51
#     print("You are going too fast you will get a fine of $45!")

# 2 Playing in a Tournament

# wins = 0
# wins = int(wins) # makes the variable an integer
# for i in range(0,6): # repeats the code inside 6 times
#     wins_input = input("Did you win or lose your game (type a W or L)")
#     if wins_input == "W":
#         wins = wins + 1 # adds one to the variable if they win
# if wins == 6: # prints they have 6 wins
#     print("W W W W W W, you have a perfect record and are advancing into the first group.")
# elif wins == 5: # prints they have 5 wins
#     print("W W W W W L, you are advancing into the first group")
# elif wins == 4: # prints they have 4 wins
#     print("W W W W L L, you are advancing into the second group")
# elif wins == 3: # prints they have 3 wins
#     print("W W W L L L, you are advancing into the second group")
# elif wins == 2: # prints they have 2 wins
#     print("W W L LL L, you are advancing into the last group")
# elif wins == 1: # prints they have 1 wins
#     print("W L L L L L, you are advancing into the last group")
# elif wins == 0: # prints they have 0 wins
#     print("L L L L L L, you are not advancing and you are eliminated")

# 3 Grade Reporting

# marks = 0
# marks = int(marks) # makes the variable an integer
# course = int(input("How many courses did you take this year?")) # finds out the amount of times to run the for loop
# for i in range(0, course):
#     mark_input = int(input("What mark did you get in one of your courses?"))
#     marks = (marks+mark_input) # adds the inputs together to get the total
# marks = (marks/course) # divides the marks by the number of courses which finds the average
# if marks >= 79.5: # prints in you got the principle's award
#     print("You got the principle's award with an average of", marks)
# if marks < 79.5: # prints in you did not get the principle's award
#     print("You did not get the principle's award but maybe next year. You got an average of", marks)

# 4 Cookies

# cookies = int(input("How many cookies so you want to buy? You have to buy a minimum 200.")) # finds amount of the int
# crates = int(cookies/(20*12)) # if the variable is divisible by the amount of cookies in a crate which is 240
# cookies = int(cookies - crates*(20 * 12)) # subtracts the amount of cookies in the crates from the total of cookies
# boxes = int(cookies/12) # if the variable is divisible by the amount of cookies in a box which is 12
# cookies = int(cookies - boxes*12) # subtracts the amount of cookies in the boxes from the total of cookies
# print("You are buying", crates, "crates.") # prints the amount of crates
# print("You are buying", boxes, "boxes.")
# print("You are buying", cookies, "individual cookies.")
# print("Your total price is $", crates*80+boxes*5+cookies*0.5) # prints the total price of all of he cookies

# 5 Advanced Math App
#
# running = 0
# while running == 0: # creates a  constant loop unless ended
#     pythagoras = 0
#     tip = 0
#     celsius = 0
#     fahrenheit = 0
#     print("Do you want to use a pythagoras calculator, tip calculator, or temperature converter?") # instructions
#     start = int(start)
#     start = input("Press 1 pythagoras calculator\nPress 2 tip calculator\nPress 3 temperature converter\nPress 4 stop")
#     if start == 1:
#         for x in range(0, 2):
#             pythagoras_input = int(input("What is one of your two numbers?"))
#             pythagoras = (pythagoras_input * pythagoras_input + pythagoras) # squares numbers and adds them together
#         pythagoras = math.sqrt(pythagoras) # square roots the number to get the hypotenuse
#         print("The hypotenuse of your triangle is", round(pythagoras, 2)) # prints and rounds the hypotenuse
#     elif start == 2:
#         bill = int(input("How much did the bill cost?"))
#         percent = int(input("What percentage do you want too tip?"))
#         tip = (bill * (percent / 100)) get percentage of bill
#         print("Your tip at", percent, "percent should be", tip) # tells you how much to tip
#     elif start == 3:
#         temp = int(input("If you want to from fahrenheit to celsius press 1 or from celsius to fahrenheit press 2"))
#         if temp == 1:
#             temp_input = int(input("What is the temperature in fahrenheit?"))
#             celsius = (temp_input - 32) * 5 / 9 # converts from fahrenheit to celsius
#             print("The temperature in celsius is", celsius) # prints the temp in celsius
#         elif temp == 2:
#             temp_input = int(input("What is the temperature in celsius?"))
#             fahrenheit = (temp_input * 9 / 5 + 32) # converts from celsius to fahrenheit
#             print("The temperature in fahrenheit is", fahrenheit)# prints the temp in fahrenheit
#     elif start == 4:
#         running = 1 # ends the loop
