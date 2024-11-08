import spacy

def delta(a, b):
   return 1 if a == b else -1

UP = (-1,0)
LEFT = (0, -1)
TOPLEFT = (-1, -1)
ORIGIN = (0, 0)

def traceback_global(v, w, pointers):
    i,j = len(v), len(w)
    new_v = []
    new_w = []
    while True:
        di, dj = pointers[i][j]
        if (di,dj) == LEFT:
            new_v.append('-')
            new_w.append(w[j-1])
        elif (di,dj) == UP:
            new_v.append(v[i-1])
            new_w.append('-')
        elif (di,dj) == TOPLEFT:
            new_v.append(v[i-1])
            new_w.append(w[j-1])
        i, j = i + di, j + dj
        if (i <= 0 and j <= 0):
            break
    return ''.join(new_v[::-1])+'\n'+''.join(new_w[::-1])

def global_align(v, w):
    """
    Returns the score of the maximum scoring alignment of the strings v and w, as well as the actual alignment as
    computed by traceback_global.

    :param: v
    :param: w
    :param: delta
    """
    M = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    pointers = [[ORIGIN for j in range(len(w)+1)] for i in range(len(v)+1)]
    score, alignment = None, None
    # YOUR CODE HERE

    M[0][0] = 0

    # v = '-' + v
    # w = '-' + w

    for i in range(len(v)+1):
      # M[0][i] = -i
      M[i][0] = -i

      # pointers[0][i] = LEFT
      pointers[i][0] = UP

    for i in range(len(w)+1):
      M[0][i] = -i
      # M[i][0] = -i

      pointers[0][i] = LEFT
      # pointers[i][0] = UP

    for i in range(1, len(v)+1):
      for j in range(1, len(w)+1):
        r = []

        if (i > 0):
            r.append(M[i - 1][j] + delta(v[i-1], '-'))

            # print("i>0", r[-1])
        else:
            r.append(-float('inf'))

        if (j > 0):
            r.append(M[i][j - 1] + delta('-', w[j-1]))
            # print("j>0", r[-1])
        else:
            r.append(-float('inf'))

        if i > 0 and j > 0:
            r.append(M[i - 1][j - 1] + delta(v[i-1], w[j-1]))
            # print("iboth", r[-1])
        else:
            r.append(-float('inf'))

        # print(i, j, max(r), max_idx)

        max_idx = r.index(max(r))

        M[i][j] = max(r)

        if max_idx == 0:
            pointers[i][j] = UP
        elif max_idx == 1:
            pointers[i][j] = LEFT
        elif max_idx == 2:
            pointers[i][j] = TOPLEFT

    score = M[-1][-1]

    # for a in M:
    #     print(a)
    # for a in pointers:
    #     print(a)

    alignment = traceback_global(v,w, pointers)
    return score, alignment

nlp = spacy.load("en_core_web_sm")

text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

for entity in doc:
    print(entity.text, entity.pos_)

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
    "PUNCT": ".",
    "SCONJ": "S",
    "SYM": "Y",
    "VERB": "V",
    "X": "X",
    "SPACE": " "
}


a = [pos_map[entity.pos_] for entity in doc]
x, y = global_align(a, a)

print(x)
print(y)