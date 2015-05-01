
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

    def __init__(self, barrel_ids, barrel_positions):
        self.__barrel_L = Enigma.BARREL[barrel_ids[0]]
        self.__barrel_M = Enigma.BARREL[barrel_ids[1]]
        self.__barrel_R = Enigma.BARREL[barrel_ids[2]]
        self.__barrel_L_position = barrel_positions[0]
        self.__barrel_M_position = barrel_positions[1]
        self.__barrel_R_position = barrel_positions[2]
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
        return barrel[Enigma.ctoi(input_char)-1]

    @staticmethod
    def barrel_encode_rev(barrel, input_char):
        return Enigma.itoc(barrel.index(input_char)+1)

    @staticmethod
    def ctoi_barrel(barrel, a):
        return Enigma.BARREL[barrel].index(a)+1

    @staticmethod
    def itoc_barrel(barrel, i):
        return Enigma.BARREL[barrel][i-1]

    @staticmethod
    def shift_char_barrel(barrel, char, shift):
        return Enigma.itoc_barrel(barrel, (Enigma.ctoi_barrel(barrel, char) + shift) % len(Enigma.BARREL[barrel]))

    def increment_barrels(self):
        self.__barrel_R_position += 1
        if self.__barrel_R_position == len(Enigma.ALPHABET):
            self.__barrel_M_position += 1
            if self.__barrel_M_position == len(Enigma.ALPHABET):
                self.__barrel_L_position += 1
                self.__barrel_L_position %= len(Enigma.ALPHABET)
            self.__barrel_M_position %= len(Enigma.ALPHABET)
        self.__barrel_R_position %= len(Enigma.ALPHABET)

    def print_barrel_positions(self):
        print "(", self.__barrel_L_position, ",", self.__barrel_M_position, ",", self.__barrel_R_position, ")"

    def encode(self, input_char):
        self.increment_barrels()
        msg = input_char
        msg = self.pinboard_encode(msg)
        msg = Enigma.barrel_encode(self.__barrel_R, self.shift_char_barrel(2, msg, -self.__barrel_R_position))
        msg = Enigma.barrel_encode(self.__barrel_M, self.shift_char_barrel(1, msg, self.__barrel_M_position))
        msg = Enigma.barrel_encode(self.__barrel_L, self.shift_char_barrel(0, msg, self.__barrel_L_position))
        msg = Enigma.UKW[0][msg]
        msg = Enigma.barrel_encode_rev(self.__barrel_L, self.shift_char_barrel(0, msg, 0))
        msg = Enigma.barrel_encode_rev(self.__barrel_M, self.shift_char_barrel(1, msg, -self.__barrel_M_position))
        msg = Enigma.barrel_encode_rev(self.__barrel_R, self.shift_char_barrel(2, msg, self.__barrel_R_position))
        msg = self.pinboard_encode(Enigma.shift_char(msg, self.__barrel_R_position))
        return msg

    def set_pinboard(self, connections):
        self.pinboard = {x[0]: x[1] for x in connections}
        self.pinboard.update({x[1]: x[0] for x in connections})

    def pinboard_encode(self, char):
        if char in self.pinboard:
            return self.pinboard[char]
        else:
            return char

eni = Enigma((0, 1, 2), (24, 25, 25))
eni.set_pinboard(['AE', 'BJ', 'CM', 'DZ', 'FL', 'GY', 'HX', 'IV', 'KW', 'NR'])
bla1 = [eni.encode('H'), eni.encode('E'), eni.encode('L'), eni.encode('L'), eni.encode('O')]
print bla1

eni2 = Enigma((0, 1, 2), (24, 25, 25))
eni2.set_pinboard(['AE', 'BJ', 'CM', 'DZ', 'FL', 'GY', 'HX', 'IV', 'KW', 'NR'])
bla2 = [eni.encode(bla1[0]), eni.encode(bla1[1]), eni.encode(bla1[2]), eni.encode(bla1[3]), eni.encode(bla1[4])]
print bla2
