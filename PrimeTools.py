from sympy.ntheory import ecm, isprime, randprime
import random
from mathPrimitives import gcd

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
