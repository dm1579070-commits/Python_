X=float(input("Вещественное число( |x|<1 ): ")) 
N=int(input("Целое число (N>0): "))
total_sum=0
sign=1
for i in range(1,N+1):
   c=sign*(X**i/i)
   total_sum+=c
   sign=-sign

print(f"Значение выражения {total_sum}")