
class Enigma():
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    BARREL = [
        "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "VZBRGITYUPSDNHLXAWMJQOFECK"
    ]

    UKW = [{
        'A': 'E', 'B': 'J', 'C': 'M', 'D': 'Z',  'F': 'L',  'G': 'Y',  'H': 'X',  'I': 'V',  'K': 'W',  'N': 'R',  
        'O': 'Q',  'P': 'U',  'S': 'T', 'E': 'A', 'J': 'B', 'M': 'C', 'Z': 'D',  'L': 'F',  'Y': 'G',  'X': 'H',
        'V': 'I',  'W': 'K',  'R': 'N',  'Q': 'O',  'U': 'P',  'T': 'S'
    }]

    def __init__(self):
        """
        self.__rotor_L = Enigma.BARREL[rotorLid]
        self.__rotor_M = Enigma.BARREL[rotorMid]
        self.__rotor_R = Enigma.BARREL[rotorRid]
        self.__rotor_L_position = 1
        self.__rotor_M_position = 1
        self.__rotor_R_position = 1
        """
        self.pinboard = {}

    @staticmethod
    def ctoi(a):
        return Enigma.ALPHABET.index(a)+1

    @staticmethod
    def itoc(i):
        return Enigma.ALPHABET[i-1]

    @staticmethod
    def shift_char(char, shift):
        return Enigma.itoc((Enigma.ctoi(char) + shift) % len(Enigma.ALPHABET))

    @staticmethod
    def barrel_encode(barrel, input_char):
        return Enigma.BARREL[barrel][Enigma.ctoi(input_char)-1]

    @staticmethod
    def barrel_encode_rev(barrel, input_char):
        return Enigma.itoc(Enigma.BARREL[barrel].index(input_char)+1)



    def set_pinboard(self, connections):
        self.pinboard = {x[0]: x[1] for x in connections}
        self.pinboard.update({x[1]: x[0] for x in connections})

    def pinboard_encode(self, char):
        if char in self.pinboard:
            return self.pinboard[char]
        else:
            return char






print Enigma.UKW[0]['L']
print Enigma.ctoi('B')
print Enigma.itoc(12)
eni = Enigma()
eni.set_pinboard(['AE', 'BJ', 'CM', 'DZ', 'FL', 'GY', 'HX', 'IV', 'KW', 'NR'])
print eni.pinboard_encode('C')
print eni.pinboard
print Enigma.shift_char('A', 1)
print Enigma.barrel_encode_rev(0, 'O')