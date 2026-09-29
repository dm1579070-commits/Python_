N=int(input("число N (>1): "))
F1=1
F2=1
while F2<N:
   F1, F2= F2,F1 + F2

print(F2==N)