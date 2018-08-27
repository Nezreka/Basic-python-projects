import math


def findNum(num):
    print(num)
    print(str('{:.{}f}'.format(math.pi, num)))


try:
    number = str(input("Enter your number for pi"))
    findNum(number)
except:
    print("You printed an invalid number")
