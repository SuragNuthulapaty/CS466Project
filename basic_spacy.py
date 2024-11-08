import spacy

def delta(a, b):
   return 1 if a == b else -1

UP = (-1,0)
LEFT = (0, -1)
TOPLEFT = (-1, -1)
ORIGIN = (0, 0)

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

text = """1. PROLOGUE

Two households, both alike in dignity,
In fair Verona, where we lay our scene,
From ancient grudge break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal loins of these two foes
A pair of star-cross'd lovers take their life;
Whose misadventured piteous overthrows
Do with their death bury their parents' strife.
The fearful passage of their death-mark'd love,
And the continuance of their parents' rage,
Which, but their children's end, nought could remove,
Is now the two hours' traffic of our stage;
The which if you with patient ears attend,
What here shall miss, our toil shall strive to mend.

2. SCENE I. Verona. A public place.

Enter SAMPSON and GREGORY, of the house of Capulet, armed with swords and bucklers.

SAMPSON
Gregory, o' my word, we'll not carry coals.

GREGORY
No, for then we should be colliers.

SAMPSON
I mean, and we be in choler, we'll draw.

GREGORY
Ay, while you live, draw your neck out of collar.

SAMPSON
I strike quickly, being moved.

GREGORY
But thou art not quickly moved to strike.

SAMPSON
A dog of the house of Montague moves me.

GREGORY
To move is to stir, and to be valiant is to stand: therefore, if thou art moved, thou runn'st away.

SAMPSON
A dog of that house shall move me to stand: I will take the wall of any man or maid of Montague's.

GREGORY
That shows thee a weak slave; for the weakest goes to the wall.

SAMPSON
True; and therefore women, being the weaker vessels, are ever thrust to the wall: therefore I will push Montague's men from the wall, and thrust his maids to the wall.

GREGORY
The quarrel is between our masters and us their men.

SAMPSON
'Tis all one, I will show myself a tyrant: when I have fought with the men, I will be cruel with the maids, and cut off their heads.

GREGORY
The heads of the maids?

SAMPSON
Ay, the heads of the maids, or their maidenheads; take it in what sense thou wilt.

GREGORY
They must take it in sense that feel it.

SAMPSON
Me they shall feel while I am able to stand: and 'tis known I am a pretty piece of flesh.

GREGORY
'Tis well thou art not fish; if thou hadst, thou hadst been poor-John. Draw thy tool! here comes two of the house of Montague.

SAMPSON
My naked weapon is out: quarrel, I will back thee.

GREGORY
How! turn thy back and run?

SAMPSON
Fear me not.

GREGORY
No, marry; I fear thee!

SAMPSON
Let us take the law of our sides; let them begin.

GREGORY
I will frown as I pass by, and let them take it as they list.

SAMPSON
I will bite my thumb at them; which is a disgrace to them, if they bear it.

GREGORY
Do you bite your thumb at us, sir?

SAMPSON
I do bite my thumb, sir.

GREGORY
Do you bite your thumb at us, sir?

SAMPSON
Is the law of our side, if I say ay?

GREGORY
No.

SAMPSON
No, sir, I do not bite my thumb at you, sir; but I bite my thumb, sir.

GREGORY
Do you quarrel, sir?

SAMPSON
Quarrel sir! no, sir.

GREGORY
But if you do, sir, I am for you: I serve as good a man as you.

SAMPSON
No better.

GREGORY
Well, sir.

SAMPSON
Say better: here comes one of my master's kinsmen.

GREGORY
Yes, better, sir.

SAMPSON
You lie.

GREGORY
Draw, if you be men. Gregory, remember thy swashing blow.

SAMPSON
They have made worms' meat of me.

GREGORY
I have it, and it is a very good sword.

SAMPSON
I will cut you, sir, I will cut you!

GREGORY
A dog of Montague! what a quarrel is this?

SAMPSON
I will cut off their heads.

GREGORY
Peace be with you.

SAMPSON
The people, sir, will riot.

GREGORY
The walls are full of them.

SAMPSON
The blood is on my hands. I will fight them. Take this fight in case it continues!
"""

doc = nlp(text)


a = doc_to_characters(doc)
x, y = global_align(a, a)

print(y)
print(x)
print(len(a))