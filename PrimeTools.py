from sympy.ntheory import ecm, isprime, randprime
import random
from mathPrimitives import gcd, ModularExponentiation

#Should implement this on my own at some point - I want to use elliptic curve primality testing
class PrimeTools:

    def factor(n):
        return list(ecm(n))
    
    def isPrime(n):
        return isprime(n)
    
    def randomPrimeBitBounded(lowerBoundBitsize=512, upperBoundBitsize=1024):
        randLow = random.getrandbits(lowerBoundBitsize)
        randHigh = random.getrandbits(upperBoundBitsize)
        randPrime = randprime(randLow, randHigh)

        while (PrimeTools.isPrime(randPrime) != True):
            randLow = random.getrandbits(lowerBoundBitsize)
            randHigh = random.getrandbits(upperBoundBitsize)
            randPrime = randprime(randLow, randHigh)
            

        return randPrime

    def randomPrimeIntBounded(lowerBound, upperBound):
        randPrime = randprime(lowerBound, upperBound)

        while (PrimeTools.isPrime(randPrime) != True):
            randPrime = randprime(lowerBound, upperBound)
        
        return randPrime



    def randomCoprime(target, lowerBound, upperBound):
        candidate = random.randrange(lowerBound, upperBound)
        while (gcd.EuclideanAlgorithm(candidate, target) > 1):
            candidate = random.randrange(lowerBound, upperBound)
        
        return candidate

    def allCoprimeIntegers(target):
        ret = []
        for i in range(1, target):
            if gcd.EuclideanAlgorithm(i, target) == 1:
                ret.append(i)
        return ret

    def isPseudoprime(n, b):
        #returns whether n is pseudoprime to base b
        return (ModularExponentiation.constantTimePower(b, n-1, n) == 1)

    def isCarmichaelNumber(n):
        #Checks if Fermat's Little Theorem is satisfied by brute force.
        for i in PrimeTools.allCoprimeIntegers(n):
            if PrimeTools.isPseudoprime(n, i) != True:
                return False
        return True

    



