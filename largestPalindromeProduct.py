def isAPalindrome(intValue):
    valueString = str(intValue);
    startIndex = 0
    endIndex = len(valueString) - 1

    while (startIndex <= endIndex):
        if (valueString[startIndex] != valueString[endIndex]):
            return False;
        startIndex = startIndex + 1
        endIndex = endIndex - 1
    return True

largestThreeDigit = 999;

largest = 0;

for value in range(largestThreeDigit, 1, -1):
    for otherValue in range(largestThreeDigit, 1, -1):
        multi = value * otherValue;
        if (isAPalindrome(multi)):

            if (largest < multi):
                largest = multi
                
print (largest)
