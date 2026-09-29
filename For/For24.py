X=float(input("Вещественное число: ")) #Я ПОПРОБОВАЛА, НО СОМНЕВАЮСЬ
N=int(input("Целое число: "))
total_sum=1
factorial=1.0
sign=1
for i in range(1,N+1):
   w=2*i
   factorial*=w
   c=sign*(X**w/factorial)
   total_sum+=c
   sign=-sign

print(f"Значение выражения {total_sum}")