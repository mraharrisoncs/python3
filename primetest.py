def ReturnPrime(x):
    c = 0
    for i in range(0,x+1):
        if c > len(prime) -1:
            c = 0
        p = prime[c]
        c = c + 1
    return p

prime = [9369319,2521008887,1442968193,10619863,6692367337]
print(ReturnPrime(0))
print(ReturnPrime(1))
print(ReturnPrime(2))
print(ReturnPrime(3))
print(ReturnPrime(4))

