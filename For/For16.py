A=float(input("Введи число: "))
N=int(input(f"Степень числа {A}: "))
c=1.0
for i in range(1, N+1):
 c*=(A)
 print(f"{A}в степени N{i}: {c}")