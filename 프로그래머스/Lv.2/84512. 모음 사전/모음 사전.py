from itertools import product as P
solution = lambda word:sorted(''.join(p) for i in range(5) for p in P('AEIOU', repeat=i+1)).index(word)+1