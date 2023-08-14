class gcd:
    def EuclideanAlgorithm(x, y):
        while y:
            x, y = y, (x % y)
        return abs(x)

class Congruences:
    def gcdExtended(a, b):
        global x, y
    
        if (a == 0):
            x = 0
            y = 1
            return b
    
        gcd = Congruences.gcdExtended(b % a, a)
        x1 = x
        y1 = y
    
        x = y1 - (b // a) * x1
        y = x1
    
        return gcd
    
    
    def modInverse(A, M):
        g = Congruences.gcdExtended(A, M)
        if (g != 1):
            return None
    
        else:
            res = (x % M + M) % M
            return res
    
    def solveLinearCongruence(y, a, b, N):
        return ((Congruences.modInverse(a, N) * y) + Congruences.modInverse(b, N)) % N
    