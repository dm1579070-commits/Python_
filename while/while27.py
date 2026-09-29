N=int(input("число N (Фибоначчи 100%(>1)): "))
F1=1
F2=1
k=2
while F2<N:
   F1, F2= F2,F1 + F2
   k+=1
print(k)