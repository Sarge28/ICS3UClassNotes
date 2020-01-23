import math
try:
    f = open("samplefile.txt", "a")
except IOError:
    print("What happened to my file")
    f = open("samplefile.txt", "x")
except ArithmeticError:
    print("Don't even try to divide by zero")
else:
    print("Success!")

try:
    print(4/0)
except ZeroDivisionError:
    print("oops tried to divide by zero")

try:
    math.sqrt(-1)
except ValueError:
    print("That’s an imaginary number")

try:
    x = str(2) + int(3)
except TypeError:
    print("That is not right try using two integers instead of a string and integer")

list1 = ["whole", "2 percent", "skim"]
try:
    print(list1[5])
except IndexError:
    list1.append("1 percent")
    list1.append("almond")
    list1.append("low fat")
    print(list1)
