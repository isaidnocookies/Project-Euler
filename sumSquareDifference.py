import math

def sumOfSquares(maxNumber):
    sum = 0;
    for i in range (0, maxNumber+1):
        sum = sum + math.pow(i, 2)

    return sum

def squareOfSum(maxNumber):
    sum = 0
    for i in range(0, maxNumber + 1):
        sum = sum + i

    return math.pow(sum, 2)

print (squareOfSum(100) - sumOfSquares(100))
