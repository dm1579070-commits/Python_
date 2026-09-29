A=float(input("Введи число: "))
N=int(input(f"Степень числа {A}: "))
total=0
sign=-1
for i in range(1, N+1):
 w=A**i
 total+=w*sign
 sign=-sign
total+=1
print(f" Значение выражения {A}: {total}")