N=int(input("Введи число N(>0): "))
factorial=1.0
for i in range(1,N+1):
    factorial*=i


print(f" Факториал  {N}: {factorial}")