N=int(input("число N (Фибоначчи 100%(>1)): "))
F1=1
F2=1
for i in range(N):
   print(F1)
   F1, F2= F2,F1 + F2