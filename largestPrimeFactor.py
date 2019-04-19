import math

def isPrime(value):
    maxValue = math.sqrt(value)
    if (value % 2 == 0):
        return False

    for i in range(3, int(maxValue) + 1, 2):
        if (value % i == 0):
            return False
    return True

def main():
    value = 600851475143
    valueRoot = int(math.sqrt(value))
    startNumber = valueRoot

    if (startNumber % 2 == 0):
        startNumber = startNumber - 1

    for i in range(startNumber, 1, -2):
        if (value % i == 0):
            if (isPrime(i)):
                print (i)
                quit()

    print ("Shit")

if __name__ == "__main__":
    main()
