from labellings import AlphabetNGraphToVector, AlphabetToInteger, TextToASCII
from AffineEncipheringMatrix import AffineEncipheringMatrix
from RSA import RSAEncryption, RSAEncrypter, RSADecrypter, RSAUtils

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

class TextRSAEncryption:
    #Converts text into ASCII, then encrypts via RSA. 
    def __init__(self):
        self.cipher = RSAEncryption()
    
    def encrypt(self, msg):
       convertedText = TextToASCII.convert(msg)
       return self.cipher.encrypt(convertedText)

    def decrypt(self, msg):
        print(msg)
        return TextToASCII.reverse(self.cipher.decrypt(msg))

    def decryptFile(self, filename):
        return TextToASCII.reverse(self.cipher.decryptFile(filename))
    
message = "Uh oh, another line of text!"
publicKeys = RSAUtils.readKeyFile("public.txt")
encrypter = RSAEncrypter(publicKeys[0], publicKeys[1])
print(encrypter.encrypt(TextToASCII.convert(message)))


    

    


