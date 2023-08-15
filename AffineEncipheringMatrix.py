from mathPrimitives import Matrix
from MatrixTools import MatrixTools

#Represent a message as a tuple of unit messages

class AffineEncipheringMatrix:
    def __init__(self, A, B, N):
        self._A = A
        self._B = B
        self._N = N

        if (abs(MatrixTools.determinant(A) - 1) > 0.1):
            raise Exception("Determinant of A needs to be one!")
    
    def encryptUnit(self, unitMsg):
        #in this case, a unit message is an n-vector represented vertically, where n is the number of rows in A
        mult = Matrix.multiplicationOverField(self._A, unitMsg, self._N)
        return Matrix.additionOverField(mult, self._B, self._N)
    
    def decryptUnit(self, unitMsg):
        AInv = MatrixTools.inverse(self._A)
        ret = Matrix.multiplicationOverField(AInv, unitMsg, self._N)
        ret2 = Matrix.multiplicationOverField(AInv, self._B, self._N)
        return Matrix.subtractionOverField(ret, ret2, self._N)
    
    def encrypt(self, msg):
        ret = ()
        for i in msg:
            ret = ret + tuple([self.encryptUnit(i)])
        return ret

    def decrypt(self, msg):
        ret = ()
        for i in msg:
            ret = ret + tuple([self.decryptUnit(i)])
        
        return ret