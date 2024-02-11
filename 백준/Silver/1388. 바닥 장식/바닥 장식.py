L = [input() for _ in range(int(input().split()[0]))]
print(sum(len([p for p in r.split('|') if p]) for r in L)+sum(len([q for q in ''.join(x).split('-') if q]) for x in zip(*L)))