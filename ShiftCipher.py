class ShiftCipher:
    def __init__(self, b, N):
        self._b = b
        self._N = N
    
    def encryptUnit(self, unitMsg):
        unitMsg = int(unitMsg)

        if (unitMsg > self._N):
            raise Exception("unit message value invalid,")

        return str(((unitMsg + self._b) %  self._N))

    def decryptUnit(self, unitMsg):
        return ShiftCipher(-1 * self._b, self._N).decryptUnit(unitMsg)

    def encrypt(self, msg):
        splitMsg = msg.split()
        ret = self.encryptUnit(splitMsg[0])

        for i in splitMsg[1:]:
            ret = ret + " " + self.encryptUnit(i)
    
        return ret

    def decrypt(self, msg):
        return ShiftCipher(-1 * self._b, self._N).encrypt(msg)
