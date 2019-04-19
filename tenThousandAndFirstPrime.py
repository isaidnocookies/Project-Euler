import math

def isPrime(value):
    maxValue = math.sqrt(value)
    if (value % 2 == 0):
        return False

    for i in range(3, int(maxValue) + 1, 2):
        if (value % i == 0):
            return False
    return True

count = 0;
index = 1;

while True:
    if (isPrime(index)):
        count += 1
        if (count == 10001):
            print (index)
            quit()
    index += 1
