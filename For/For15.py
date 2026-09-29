A=float(input ("Число А: ")) #Сделан
N=int(input ("Степень числа A: "))
cost=1
for i in range (1, N+1):
  cost*=A

print (f"{A} в степени {N} будет: {cost}")