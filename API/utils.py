UP = (-1,0)
LEFT = (0, -1)
TOPLEFT = (-1, -1)
ORIGIN = (0, 0)

def delta(a, b):
   return 1 if a == b else -1

def doc_to_characters(doc):
    pos_map = {
        "ADJ": "A",
        "ADP": "P",
        "ADV": "R",
        "AUX": "X",
        "CCONJ": "C",
        "DET": "D",
        "INTJ": "I",
        "NOUN": "N",
        "NUM": "M",
        "PART": "T",
        "PRON": "O",
        "PROPN": "P",
        "PUNCT": "U",
        "SCONJ": "S",
        "SYM": "Y",
        "VERB": "V",
        "X": "X",
        "SPACE": "E"
    }


    return [pos_map[entity.pos_] for entity in doc]