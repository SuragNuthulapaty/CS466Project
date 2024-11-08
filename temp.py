import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define sequences and scoring scheme
seq1 = "AGTACGCA"
seq2 = "TATGC"
match_score = 1
mismatch_score = -1
gap_penalty = -2

# Initialize the DP matrix
dp_matrix = np.zeros((len(seq1) + 1, len(seq2) + 1), dtype=int)

# Fill the DP matrix
for i in range(1, len(seq1) + 1):
    dp_matrix[i][0] = dp_matrix[i-1][0] + gap_penalty
for j in range(1, len(seq2) + 1):
    dp_matrix[0][j] = dp_matrix[0][j-1] + gap_penalty

for i in range(1, len(seq1) + 1):
    for j in range(1, len(seq2) + 1):
        match = dp_matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_score)
        delete = dp_matrix[i-1][j] + gap_penalty
        insert = dp_matrix[i][j-1] + gap_penalty
        dp_matrix[i][j] = max(match, delete, insert)

# Plot the DP matrix as an image
plt.figure(figsize=(10, 8))
sns.heatmap(dp_matrix, annot=True, fmt="d", xticklabels=[''] + list(seq2), yticklabels=[''] + list(seq1))
plt.title("Global Alignment DP Matrix")
plt.xlabel("Sequence 2")
plt.ylabel("Sequence 1")
plt.show()
