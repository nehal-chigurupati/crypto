from mathPrimitives import gcd, Congruences
class AffineCipher:
    def __init__(self, a, b, N):
        self._a = a
        self._b = b
        self._N = N

        if gcd.EuclideanAlgorithm(self._b, self._N) != 1:
            raise Exception("gcd(b, N) must be 1 for linear congruence to have unique solution!")
    
    def encryptUnit(self, unitMsg):
        unitMsg = int(unitMsg)
        return str(((self._a * int(unitMsg)) + self._b) % self._N)

    def decryptUnit(self, unitMsg):
        unitMsg = int(unitMsg)
        return str(Congruences.solveLinearCongruence(unitMsg, self._a, self._b, self._N))

    def encrypt(self, msg):
        splitMsg = msg.split()
        ret = self.encryptUnit(splitMsg[0])

        for i in splitMsg[1:]:
            ret = ret + " " + self.encryptUnit(i)
        
        return ret

    def decrypt(self, msg):
        splitMsg = msg.split()
        ret = self.decryptUnit(splitMsg[0])

        for i in splitMsg[1:]:
            ret = ret + " " + self.decryptUnit(i)
        
        return ret

