X=float(input("Вещественное число: "))
N=int(input("Целое число: "))
total_sum=1.0
factorial=1.0
for i in range(1,N+1):
   factorial*=i
   c=X**i/factorial
   total_sum+=c

print(f"Сумма {total_sum}")