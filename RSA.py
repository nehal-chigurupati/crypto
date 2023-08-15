from mathPrimitives import gcd, Congruences, ModularExponentiation
from PrimeTools import PrimeTools

class RSAEncryption:
    def __init__(self):
        self._p = PrimeTools.randomPrimeBitBounded()
        self._q = PrimeTools.randomPrimeBitBounded()
        self.n = self._p * self._q
        self._phin = (self._p - 1)*(self._q - 1)
        self.e = PrimeTools.randomPrimeIntBounded(2, max(self._p, self._q))
        self._d = Congruences.modInverse(self.e, self._phin)
    
    def encryptUnit(self, unitMsg):
        #here, unitMsg is a character that represents an integer
        return str(ModularExponentiation.constantTimePower(int(unitMsg), self.e, self.n))

    def decryptUnit(self, unitMsg):
        return str(ModularExponentiation.constantTimePower(int(unitMsg), self._d, self.n))

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

    def publickey(self):
        return (self.n, self.e)
