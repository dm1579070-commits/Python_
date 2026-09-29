N=int(input("число N (Фибоначчи 100%): "))
F1=1
F2=1
while F2<N:
   F1, F2= F2,F1 + F2

print(F1)
print(F2+F1)