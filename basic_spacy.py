import spacy
import global_alignment
import local_alignment
import fitting_alignment
import utils

nlp = spacy.load("en_core_web_sm")

text = """
The world of quantum physics is a vast and mysterious realm, where particles behave in ways that defy classical logic. At the subatomic level, everything is probabilistic, and the very act of observing a particle can alter its state. Quantum entanglement, a phenomenon where particles become linked across vast distances, challenges our understanding of space and time. Despite these perplexing concepts, physicists continue to explore this strange world, making discoveries that could eventually lead to advancements in computing, cryptography, and our understanding of the universe itself.
"""
text2 = """
On the edge of the town, a small café stood quietly, its windows fogged with the warmth of brewing coffee inside. The air was filled with the scent of freshly baked pastries and the soft hum of conversation. An elderly man sat by the window, sipping his coffee slowly as he watched the rain fall in sheets. Outside, people hurried by, some with umbrellas, others trying to shield themselves with newspapers. The world seemed to move quickly, but in this little café, time felt like it had stopped, if only for a moment.
"""

doc = nlp(text)
doc2 = nlp(text2)


a = utils.doc_to_characters(doc)
b = utils.doc_to_characters(doc2)

g = global_alignment.GlobalAlignment()
l = local_alignment.LocalAlignment()
f = fitting_alignment.FittingAlignment()

x, y = g.align(a, b)
v, w = l.align(a, b)
t, u = f.align(a, b)

print("\nGLOBAL ALIGNMENT")
print(y)
print(x)

print("\nLOCAL ALIGNMENT")
print(w)
print(v)

print("\nFITTING ALIGNMENT")
print(u)
print(t)
