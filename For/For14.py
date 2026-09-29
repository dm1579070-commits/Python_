N=int(input("Введи число N(>0): "))
c=0
for i in range(1, N+1):
 w=2*i-1
 c+=w
 print(f"Число {i}, Сумма: {c}")