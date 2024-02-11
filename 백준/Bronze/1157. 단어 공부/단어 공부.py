W, n = input().upper(), 0
for c in map(chr, range(ord('A'), ord('Z')+1)):
  k = W.count(c)
  if n<k:
    m, n = c, k
  elif n==k:
    m = '?'
print(m)