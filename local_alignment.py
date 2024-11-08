import alignment
import utils

class LocalAlignment(alignment.Align):

    def traceback(self, v, w, M, init_i, init_j, pointers):
        i,j = init_i, init_j
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
            if (M[i][j] == 0):
                break
        return ''.join(new_v[::-1]) + '\n'+''.join(new_w[::-1])

    def align(self, v, w):
        M = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
        pointers = [[utils.ORIGIN for j in range(len(w)+1)] for i in range(len(v)+1)]
        score = None
        init_i, init_j = 0,0
        # YOUR CODE HERE

        M[0][0] = 0
        for i in range(len(v)+1):
            M[i][0] = 0
            pointers[i][0] = utils.ORIGIN

        for i in range(len(w)+1):
            M[0][i] = 0
            pointers[0][i] = utils.ORIGIN

        for i in range(1, len(v)+1):
            for j in range(1, len(w)+1):
                r = []

                if (i > 0):
                    r.append(M[i - 1][j] + utils.delta(v[i-1], '-'))

                    # print("i>0", r[-1])
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

                r.append(0)

                max_idx = r.index(max(r))


                M[i][j] = max(r)

                if max_idx == 0:
                    pointers[i][j] = utils.UP
                elif max_idx == 1:
                    pointers[i][j] = utils.LEFT
                elif max_idx == 2:
                    pointers[i][j] = utils.TOPLEFT
                else:
                    pointers[i][j] = utils.ORIGIN

            # bottom right most cell will have i = len(v) and j = 0

            mv = -1

            for i in range(len(v), -1, -1):
                for j in range(len(w), -1, -1):
                    if M[i][j] > mv:
                        mv = M[i][j]
                        init_i = i
                        init_j = j

        score = mv

        alignment = self.traceback(v, w, M, init_i, init_j , pointers)
        return score, alignment