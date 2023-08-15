from mathPrimitives import gcd, Congruences, ModularExponentiation
from PrimeTools import PrimeTools

class RSAEncrypter:
    def __init__(self, n, e):
        self.n = int(n)
        self.e = int(e)
    
    def encryptUnit(self, unitMsg):
        return str(ModularExponentiation.constantTimePower(int(unitMsg), self.e, self.n))

    def encrypt(self, msg):
        splitMsg = msg.split()
        ret = self.encryptUnit(splitMsg[0])
        for i in splitMsg[1:]:
            ret = ret + " " + self.encryptUnit(i)
        
        return ret

class RSADecrypter:
    def __init__(self, n, d):
        self.n = int(n)
        self._d = int(d)

    def decryptUnit(self, unitMsg):
        return str(ModularExponentiation.constantTimePower(int(unitMsg), self._d, self.n))
    
    def decrypt(self, msg):
        splitMsg = msg.split()
        ret = self.decryptUnit(splitMsg[0])
        for i in splitMsg[1:]:
            ret = ret + " " + self.decryptUnit(i)
        
        return ret


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

    def getEncrypter(self):
        return RSAEncrypter(self.n, self.e)

    def getDecrypter(self):
        return RSADecrypter(self.n, self._d)
    
    def generatePublicKeyFile(self, filename):
        f = open(filename, "w")
        f.write("(")
        f.write(str(self.n))
        f.write(",")
        f.write(str(self.e))
        f.write(")")
        f.close()
    
    def generatePrivateKeyFile(self, filename):
        f = open(filename, "w")
        f.write("(")
        f.write(str(self.n))
        f.write(",")
        f.write(str(self._d))
        f.write(")")
        f.close()
    


class RSAUtils:
    def readKeyFile(filename):
        f = open(filename, "r")
        data = f.read()
        f.close()
        data = data.replace("(", "")
        data = data.replace(")", "")
        data = data.split(",")
        return (data[0], data[1])
