
class Enigma():
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

    def __init__(self, rotorLid, rotorMid, rotorRid):
        __rotor_L = Enigma.BARREL[rotorLid]
        __rotor_M = Enigma.BARREL[rotorMid]
        __rotor_R = Enigma.BARREL[rotorRid]
        __rotor_L_position = 1
        __rotor_M_position = 1
        __rotor_R_position = 1


print Enigma.UKW[0]['L']