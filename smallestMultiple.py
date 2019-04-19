def isDivisbleByAllTo20(value):
    for i in range(2, 20):
        if (value % i != 0):
            return False
    return True

index = 20
while (True):
    if (isDivisbleByAllTo20(index)):
        print (index)
        quit()
    index = index + 20
