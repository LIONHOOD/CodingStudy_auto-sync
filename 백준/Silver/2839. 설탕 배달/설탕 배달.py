N = int(input())
print([N//5+[0,1,2,1,2][N%5],-1][N in [4,7]])