import math


def findNum(num):
    print(str('{:.{}f}'.format(math.exp(1), num)))


try:
    number = str(input("Enter your number for e"))
    findNum(number)
except:
    print("You printed an invalid number")
