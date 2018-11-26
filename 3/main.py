import pandas as pd
import sys
import numpy as np
import libcl

# processing input
pos_k = sys.argv.index('-k')
files = sys.argv[1:pos_k]
k = int(sys.argv[pos_k+1])
letters = sys.argv[pos_k+3:]

# pretty-print
def histogram(text, chars):
    # return a dictionary mapping chars to their freq
    dic = {c : 0 for c in chars}
    for x in text:
        if x in chars:
            dic[x] += 1
    return {x : dic[x]/sum(dic.values()) for x in dic}

A = pd.DataFrame(index=files, columns=letters, dtype=float)

for F in files:
    with open(F) as f:
           A.loc[F] = histogram(f.read().lower(), letters)
print(A.round(2))
 
# solution    
hc = libcl.CompleteLinkage(A.values, k)
out, clus = [], dict(hc.clusters)

# iterating over clusters
for value in clus.values():
    out.append([A.index[sub_value] for sub_value in value])

# pretty-print
for i, c in enumerate(out):
    print(i, *c)