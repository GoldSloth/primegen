import math
import time

startms = int(round(time.time() * 1000))

foundprimes = []

def testCandidate(number, existingprimes):
    for factortotest in existingprimes:
        if (number % factortotest == 0):
            return False
        elif (factortotest > math.sqrt(number)):
            return True
    if (number != 1):
        return True
    else:
        return False
        

for primetotest in range(1, 1000000):
    if (testCandidate(primetotest, foundprimes)):
        foundprimes.append(primetotest)

endms = int(round(time.time() * 1000))

print(endms-startms)

with open('primes.txt', 'w') as f:
    for item in foundprimes:
        f.write(str(item) + '\n')

