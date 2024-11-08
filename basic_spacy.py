import spacy

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

def delta(a, b):
   return 1 if a == b else -1

def global_align(v, w):
    """
    Returns the score of the maximum scoring alignment of the strings v and w, as well as the actual alignment as
    computed by traceback_global.

    :param: v
    :param: w
    :param: delta
    """
    M = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    # pointers = [[ORIGIN for j in range(len(w)+1)] for i in range(len(v)+1)]
    score, alignment = None, None
    # YOUR CODE HERE

    M[0][0] = 0

    # v = '-' + v
    # w = '-' + w

    for i in range(len(v)+1):
      # M[0][i] = -i
      M[i][0] = -i

    #   # pointers[0][i] = LEFT
    #   pointers[i][0] = UP

    for i in range(len(w)+1):
      M[0][i] = -i
      # M[i][0] = -i

    #   pointers[0][i] = LEFT
    #   # pointers[i][0] = UP

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

        M[i][j] = max(r)

        # if max_idx == 0:
        #     pointers[i][j] = UP
        # elif max_idx == 1:
        #     pointers[i][j] = LEFT
        # elif max_idx == 2:
        #     pointers[i][j] = TOPLEFT

    score = M[-1][-1]

    # for a in M:
    #     print(a)
    # for a in pointers:
    #     print(a)
    return score


a = [entity.pos_ for entity in doc]
print(global_align(a, a))