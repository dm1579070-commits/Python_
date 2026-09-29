A=float(input("Введи число: "))
N=int(input(f"Степень числа {A}: "))
sum=1.0
for i in range(1, N+1):
 w=A**i
 sum+=w
 
print(f"Сумма {A}: {sum}")