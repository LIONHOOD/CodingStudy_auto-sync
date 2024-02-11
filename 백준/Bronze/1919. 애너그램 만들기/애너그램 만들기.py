A,B = input(),input()
print(sum(abs(A.count(k)-B.count(k)) for k in {*(A+B)}))