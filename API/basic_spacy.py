import spacy
import global_alignment
import local_alignment
import fitting_alignment
import utils
import matplotlib.pyplot as plt
import seaborn as sns

THRESHOLD_VALS = 500

nlp = spacy.load("en_core_web_sm")

text = """
The world of quantum physics is a vast and mysterious realm, where particles behave in ways that defy classical logic. At the subatomic level, everything is probabilistic, and the very act of observing a particle can alter its state. Quantum entanglement, a phenomenon where particles become linked across vast distances, challenges our understanding of space and time. Despite these perplexing concepts, physicists continue to explore this strange world, making discoveries that could eventually lead to advancements in computing, cryptography, and our understanding of the universe itself.
"""
text2 = """
On the edge of the town, a small café stood quietly, its windows fogged with the warmth of brewing coffee inside. The air was filled with the scent of freshly baked pastries and the soft hum of conversation. An elderly man sat by the window, sipping his coffee slowly as he watched the rain fall in sheets. Outside, people hurried by, some with umbrellas, others trying to shield themselves with newspapers. The world seemed to move quickly, but in this little café, time felt like it had stopped, if only for a moment.
"""

text = """
The world of quantum
"""
text2 = """
On the edge of the town, a small café stood 
"""

doc = nlp(text)
doc2 = nlp(text2)


a = utils.doc_to_characters(doc)
b = utils.doc_to_characters(doc2)

g = global_alignment.GlobalAlignment()
l = local_alignment.LocalAlignment()
f = fitting_alignment.FittingAlignment()

x, y, mg, gve, gwe = g.align(a, b)
v, w, ml, lve, lwe = l.align(a, b)
t, u, mf, fve, fwe = f.align(a, b)

plt.figure(figsize=(10, 8))

cur = (mg, gve, gwe, "Global Alignment DP Matrix")
if len(cur[0]) * len(cur[0][0]) < THRESHOLD_VALS:
    sns.heatmap(cur[0], annot=True, fmt="d", cmap="Blues", xticklabels=list(cur[2]), yticklabels=list(cur[1]))
else:
    sns.heatmap(cur[0], annot=False, cmap="Blues", xticklabels=list(cur[2]), yticklabels=list(cur[1]))

plt.title(cur[3])
plt.xlabel("Sequence 2")
plt.ylabel("Sequence 1")
plt.savefig("API/static/global_align.png")
plt.clf()

cur = (mf, fve, fwe, "Fitting Alignment DP Matrix")
if len(cur[0]) * len(cur[0][0]) < THRESHOLD_VALS:
    sns.heatmap(cur[0], annot=True, fmt="d", cmap="Blues", xticklabels=list(cur[2]), yticklabels=list(cur[1]))
else:
    sns.heatmap(cur[0], annot=False, cmap="Blues", xticklabels=list(cur[2]), yticklabels=list(cur[1]))

plt.title(cur[3])
plt.xlabel("Sequence 2")
plt.ylabel("Sequence 1")
plt.savefig("API/static/fitting_align.png")
plt.clf()

cur = (ml, lve, lwe, "Local Alignment DP Matrix")
if len(cur[0]) * len(cur[0][0]) < THRESHOLD_VALS:
    sns.heatmap(cur[0], annot=True, fmt="d", cmap="Blues", xticklabels=list(cur[2]), yticklabels=list(cur[1]))
else:
    sns.heatmap(cur[0], annot=False, cmap="Blues", xticklabels=list(cur[2]), yticklabels=list(cur[1]))

plt.title(cur[3])
plt.xlabel("Sequence 2")
plt.ylabel("Sequence 1")
plt.savefig("API/static/local_align.png")
plt.clf()
