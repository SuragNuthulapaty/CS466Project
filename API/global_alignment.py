import alignment
import utils

class GlobalAlignment(alignment.Align):
    def traceback(self, v, w, M, init_i, init_j, pointers):
        i,j = len(v), len(w)
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
            if (i <= 0 and j <= 0):
                break
        return ''.join(new_v[::-1])+'\n'+''.join(new_w[::-1])

    def align(self, v, w):
        M = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
        pointers = [[utils.ORIGIN for j in range(len(w)+1)] for i in range(len(v)+1)]
        score, alignment = None, None
        # YOUR CODE HERE

        M[0][0] = 0

        # v = '-' + v
        # w = '-' + w

        for i in range(len(v)+1):
        # M[0][i] = -i
            M[i][0] = -i

            # pointers[0][i] = LEFT
            pointers[i][0] = utils.UP

        for i in range(len(w)+1):
            M[0][i] = -i
            # M[i][0] = -i

            pointers[0][i] = utils.LEFT
        # pointers[i][0] = UP

        for i in range(1, len(v)+1):
            for j in range(1, len(w)+1):
                r = []

                if (i > 0):
                    r.append(M[i - 1][j] + utils.delta(v[i-1], '-'))
                else:
                    r.append(-float('inf'))

                if (j > 0):
                    r.append(M[i][j - 1] + utils.delta('-', w[j-1]))
                else:
                    r.append(-float('inf'))

                if i > 0 and j > 0:
                    r.append(M[i - 1][j - 1] + utils.delta(v[i-1], w[j-1]))
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

        score = M[-1][-1]

        alignment = self.traceback(v, w, None, -1, -1, pointers)
        return score, alignment, M, [''] + v, [''] + w