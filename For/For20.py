N=int(input("Целое число: "))
total_sum=0.0
factorial=1.0
for i in range(1,N+1):
   factorial*=i
   total_sum+=factorial
   
   
print(f"Сумма {total_sum}")