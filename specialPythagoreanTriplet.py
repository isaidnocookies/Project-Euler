import math

for c in range(1, 1001):
    for b in range(1, c):
        for a in range(1, b):
            if (math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)):
                if (a + b + c == 1000):
                    print (a * b * c)
                    quit()
