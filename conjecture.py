import math


def theWork(num, count):
    if num == 1:
        print(count)
    elif num % 2 == 0:
        count+=1
        theWork(num / 2, count)
    else:
        count+=1
        theWork((num * 3) + 1, count)

try:
    number = int(input("Enter your number > 1"))
    theWork(number, 0)
except:
    print("You printed an invalid number")