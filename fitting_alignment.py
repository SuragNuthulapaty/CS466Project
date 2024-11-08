import alignment
import utils

class FittingAlignment(alignment.Align):
    def traceback(self, v, w, M, init_i, init_j, pointers):
        i, j = len(v), init_j
        new_v = []
        new_w = []
        while True:
            di, dj = pointers[i][j]
            if (di,dj) == utils.LEFT:
                new_v.append('-')
                new_w.append(w[j-1])
            elif (di,dj) == utils.UP:
                new_v.append(v[i-1])
                new_w.append('-')
            elif (di,dj) == utils.TOPLEFT:
                new_v.append(v[i-1])
                new_w.append(w[j-1])
            i, j = i + di, j + dj
            if (i <= 0):
                break
        return ''.join(new_v[::-1]) + '\n'+''.join(new_w[::-1])

    def align(self, short, reference):
        M = [[0 for j in range(len(reference)+1)] for i in range(len(short)+1)]
        pointers = [[utils.ORIGIN for j in range(len(reference)+1)] for i in range(len(short)+1)]
        score = None
        init_j = 0

        for i in range(len(reference) + 1):
            M[0][i] = 0

        for i in range(1, len(short)+1):
            M[i][0] = -i
            pointers[i][0] = utils.UP

        for i in range(1, len(short)+1):
            for j in range(1, len(reference)+1):
                r = []
                if (i > 0):
                    r.append(M[i - 1][j] + utils.delta(short[i-1], '-'))
                else:
                    r.append(-float('inf'))
                if (j > 0):
                    r.append(M[i][j - 1] + utils.delta('-', reference[j-1]))
                else:
                    r.append(-float('inf'))
                if i > 0 and j > 0:
                    r.append(M[i - 1][j - 1] + utils.delta(short[i-1], reference[j-1]))
                else:
                    r.append(-float('inf'))

                max_idx = r.index(max(r))
                M[i][j] = max(r)

                if max_idx == 0:
                    pointers[i][j] = utils.UP
                elif max_idx == 1:
                    pointers[i][j] = utils.LEFT
                elif max_idx == 2:
                    pointers[i][j] = utils.TOPLEFT

        score = -float('inf')
        for i, s in enumerate(M[-1][::-1]):
            if s > score:
                score = s
                init_j = len(M[-1]) - i - 1


        alignment = self.traceback(short, reference, None, -1, init_j, pointers)
        return score, alignment