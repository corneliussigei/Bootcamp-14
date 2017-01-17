def genPrimes(n):
    primeNums = []
    for i in range(2, n + 1):
        numIsPrime = True
        for k in range(2, i):
            if i % k == 0:
                numIsPrime = False
                break
        if numIsPrime == True:
            primeNums.append(i)
    return primeNums
