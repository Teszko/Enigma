
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
        'V': 'I',  'W': 'K',  'R': 'N',  'Q': 'O',  'U': 'P',  'T': 'S'},
        {
        'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L', 'I': 'P', 'J': 'X', 'K': 'N',
        'M': 'O', 'T': 'Z', 'V': 'W', 'Y': 'A', 'R': 'B', 'U': 'C', 'H': 'D', 'Q': 'E', 'S': 'F', 'L': 'G',
        'P': 'I', 'X': 'J', 'N': 'K', 'O': 'M', 'Z': 'T', 'W': 'V'}]

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
        return Enigma.itoc((Enigma.ctoi(char) + shift - 1) % len(Enigma.ALPHABET) + 1)

    @staticmethod
    def barrel_encode(barrel, input_char, rot):
        ret = Enigma.shift_char(input_char, -rot)
        ret = barrel[Enigma.ctoi(ret)-1]
        return Enigma.shift_char(ret, rot)

    @staticmethod
    def barrel_encode_rev(barrel, input_char, rot):
        ret = Enigma.shift_char(input_char, -rot)
        ret = Enigma.itoc(barrel.index(ret)+1)
        return Enigma.shift_char(ret, rot)

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
        msg = Enigma.barrel_encode(self.__barrel_R, msg, self.__barrel_R_position)
        msg = Enigma.barrel_encode(self.__barrel_M, msg, self.__barrel_M_position)
        msg = Enigma.barrel_encode(self.__barrel_L, msg, self.__barrel_L_position)
        msg = Enigma.UKW[1][msg]
        msg = Enigma.barrel_encode_rev(self.__barrel_L, msg, self.__barrel_L_position)
        msg = Enigma.barrel_encode_rev(self.__barrel_M, msg, self.__barrel_M_position)
        msg = Enigma.barrel_encode_rev(self.__barrel_R, msg, self.__barrel_R_position)
        msg = self.pinboard_encode(msg)
        return msg

    def encode_text(self, text):
        encoded_text = ""
        text = text.replace(" ", "")
        for c in text:
            encoded_text += self.encode(c)
        return encoded_text

    def set_pinboard(self, connections):
        self.pinboard = {x[0]: x[1] for x in connections}
        self.pinboard.update({x[1]: x[0] for x in connections})

    def pinboard_encode(self, char):
        if char in self.pinboard:
            return self.pinboard[char]
        else:
            return char



eni = Enigma((0, 3, 2), (15, 25, 7))
eni.set_pinboard(['AD', 'CN', 'ET', 'FL', 'GI', 'JV', 'KZ', 'PU', 'QY', 'WX'])
code = eni.encode_text(
"DASOB ERKOM MANDO DERWE HRMAQ TGIBT BEKAN NTXAA CHENX AACHE" +
"NXIST GERET TETXD URQGE BUEND ELTEN EINSA TZDER HILFS KRAEF" +
"TEKON NTEDI EBEDR OHUNG ABGEW ENDET UNDDI ERETT UNGDE RSTAD" +
"TGEGE NXEIN SXAQT XNULL XNULL XUHRS IQERG ESTEL LTWER DENX")
print code

eni = Enigma((0, 3, 2), (15, 25, 7))
eni.set_pinboard(['AD', 'CN', 'ET', 'FL', 'GI', 'JV', 'KZ', 'PU', 'QY', 'WX'])
print eni.encode_text(code)

print "\n***************************\n"