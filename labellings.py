import string

class AlphabetToInteger:
    def convertLetter(letter):
        letter = letter.upper()
        uppercaseLetters = list(string.ascii_uppercase)
        return str(uppercaseLetters.index(letter))
    
    def reverseLetter(integer):
        return list(string.ascii_uppercase)[int(integer)]

    def convert(message):
        msg = message.split()
        ret = AlphabetToInteger.convertLetter(msg[0])
        for i in msg[1:]:
            ret = ret + " " + AlphabetToInteger.convertLetter(i)
        
        return ret

    def reverse(message):
        msg = message.split()
        ret = AlphabetToInteger.reverseLetter(msg[0])
        for i in msg[1:]:
            ret = ret + " " + AlphabetToInteger.reverseLetter(i)
        
        return ret


class AlphabetNGraphToVector:
    def convertLetters(letters):
        ret = []
        for i in [*letters]:
            ret.append([int(AlphabetToInteger.convertLetter(i))])
        
        return ret

    def reverseLetters(vector):
        ret = AlphabetToInteger.reverseLetter(vector[0][0])
        for i in range(1, len(vector)):
            ret = ret + AlphabetToInteger.reverseLetter(vector[i][0])
        
        return ret

    def convert(message):
        msg = message.split()
        ret = tuple([AlphabetNGraphToVector.convertLetters(msg[0])])
        for i in msg[1:]:
            ret = ret + tuple([AlphabetNGraphToVector.convertLetters(i)])
        
        return ret

    def reverse(message):
        ret = AlphabetNGraphToVector.reverseLetters(message[0])

        for i in message[1:]:
            ret = ret + " " + AlphabetNGraphToVector.reverseLetters(i)
        
        return ret

    def splitIntoNSegments(msg, N):
        if (len(msg) % N) != 0:
            raise Exception("Improper message length")
        i = N
        ret = msg[0:i]
        while i < len(msg):
            ret = ret + " " + msg[i:i+N]
            i = i + N
        
        return ret

class TextToASCII:
    def convert(text):
        chars = list(text)
        ret = str(ord(chars[0]))
        
        for i in chars[1:]:
            ret = ret + " " + str(ord(i))

        return ret
    
    def reverse(val):
        nums = val.split()
        ret = chr(int(nums[0]))

        for i in nums[1:]:
            ret = ret + chr(int(i))
        
        return ret



        
    
