a,b = map(int,input().split())
m = a*b
while a%b!=0:
  a,b = b,a%b
print(b)
print(m//b)