from labellings import AlphabetNGraphToVector
from AffineEncipheringMatrix import AffineEncipheringMatrix

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

message = "HELLOSIR"
A = [[1, 3], [1, 4]]
B = [[1], [23]]
cipher = AlphabetAffineMatrixEncryption(A, B, 2)
ciphertext = cipher.encrypt(message)
recoveredmessage = cipher.decrypt(ciphertext)

print(message)
print(ciphertext)
print(recoveredmessage)


