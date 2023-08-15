from labellings import AlphabetNGraphToVector, AlphabetToInteger
from AffineEncipheringMatrix import AffineEncipheringMatrix
from RSA import RSAEncryption

class AlphabetAffineMatrixEncryption:
    def __init__(self, A, B, wordLength):
        self._wordLength = wordLength
        self._A = A
        self._B = B
        self._N = 26
        self._cipher = AffineEncipheringMatrix(self._A, self._B, self._N)

    def encrypt(self, message):
        plaintext = AlphabetNGraphToVector.convert(AlphabetNGraphToVector.splitIntoNSegments(message, self._wordLength))
        ciphertext = self._cipher.encrypt(plaintext)

        return ciphertext

    def decrypt(self, message):
        plaintext = self._cipher.decrypt(message)
        originalMessage = AlphabetNGraphToVector.reverse(plaintext)
        originalMessage = originalMessage.replace(" ", "")
        return originalMessage

"""
message = "HELLOSIRS"
A = [[1, 3], [1, 4]]
B = [[1], [23]]
cipher = AlphabetAffineMatrixEncryption(A, B, 2)
ciphertext = cipher.encrypt(message)
recoveredmessage = cipher.decrypt(ciphertext)

print(message)
print(ciphertext)
print(recoveredmessage)
"""

class AlphabetRSAEncryption:
    def __init__(self):
        self.cipher = RSAEncryption()
    
    def encryptLetter(self, unitMsg):
        return self.cipher.encrypt(AlphabetToInteger.convertLetter(unitMsg))

    def decryptLetter(self, unitMsg):
        return AlphabetToInteger.reverseLetter(self.cipher.decrypt(unitMsg))

    def encrypt(self, msg):
        #no spaces assumed here
        letters = list(msg)
        ret = self.encryptLetter(letters[0])

        for i in letters[1:]:
            ret = ret + " " + self.encryptLetter(i)
        
        return ret

    def decrypt(self, msg):
        split = msg.split()
        ret = self.decryptLetter(split[0])

        for i in split[1:]:
            ret = ret + " " + self.decryptLetter(i)
        
        return ret


    

    


