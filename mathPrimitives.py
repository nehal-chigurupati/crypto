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

class Matrix:
    def getColumn(arr, ind):
        res = []
        for i in arr:
            res.append(i[ind])
        
        return res
    
    def dotProductOverField(A, B, N):
        if len(A) != len(B):
            raise Exception("Incompatible dimensions!")
        
        sum = 0
        for i in range(len(A)):
            sum += ((A[i] * B[i]))
        
        return sum % N
    
    def multiplicationOverField(A, B, N):
        numRowsInA = len(A)
        numColumnsInB = len(B[0])

        res = [None] * numRowsInA

        for i in range(numRowsInA):
            currEntry = [None] * numColumnsInB
            for j in range(numColumnsInB):
                currEntry[j] = Matrix.dotProductOverField(A[i], Matrix.getColumn(B, j), N)
            
            res[i] = currEntry
        
        return res

    def additionOverField(A, B, N):
        if len(A) != len(B):
            raise Exception("Incompatible dimension!")
        if len(A[0]) != len(B[0]):
            raise Exception("Incompatible dimension!")
    
        res = [None] * len(A)
        for i in range(len(A)):
            currEntry = [None] * len(A[0])
            for j in range(len(A[0])):
                currEntry[j] = (A[i][j] + B[i][j]) % N
        
            res[i] = currEntry
        
        return res