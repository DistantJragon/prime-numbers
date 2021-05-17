import math
primeList = [2]
currentNumber = 3
currentNumberIsPrime = True
numberOfNumbersInPrimePrintList = 0
printPrimeList = [2]
printPrimeString = ''
upperBound = 100
while currentNumber < upperBound:
    for i in primeList:
        if currentNumber % i == 0:
            currentNumberIsPrime = False
            break
        if i > pow(currentNumber, 1/2):
            break
    if currentNumberIsPrime == True:
        primeList.append(currentNumber)
        printPrimeList.append(currentNumber)
        numberOfNumbersInPrimePrintList += 1
    if len(printPrimeList) >= 10:
        for prime in printPrimeList:
            printPrimeString = printPrimeString + str(prime) + ' '
        print(printPrimeString, 'List Length: ' + str(len(primeList)))
        printPrimeList = []
        printPrimeString = ''
    currentNumber += 1
    currentNumberIsPrime = True