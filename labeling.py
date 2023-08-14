class labelling:
    def __init__(self, mapping):
        self.mapping = mapping
        self.reverse = {}

        for i in self.mapping.keys():
            self.reverse[self.mapping[i]] = i
        
    
    def convert(self, msg):
        splitString = msg.split()
        ret = self.mapping[splitString[0]]
        for i in splitString[1:]:
            ret = ret + " " + self.mapping[i]
        
        return ret

    def reverse(self, msg):
        splitString = msg.split()
        ret = self.reverse[splitString[0]]
        for i in splitString[1:]:
            ret = ret + " " + self.reverse[i]
        
        return ret
