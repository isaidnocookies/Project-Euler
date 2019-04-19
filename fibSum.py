def fib(index):
    if (index <= 2):
        return index;

    return fib(index - 1) + fib(index - 2);

def main():
    sum = 0;
    index = 0;
    while(1==1):
        fibNumber = fib(index)
        if (fibNumber > 4000000):
            print (sum)
            quit()
        else:
            if (fibNumber % 2 == 0):
                sum = sum + fibNumber
        index = index + 1

main()
