X=float(input("Вещественное число( |x|<1 ): ")) #Проверить потом (+)
N=int(input("Целое число (N>0): "))
total_sum=X
sign=-1
for i in range(1,N+1):
   c=2*i+1 #СТЕПЕНЬ Х
   w=X**c 
   a2=2*i+1 #знаменатель
   sum=sign*(w/a2)  #Итог
   total_sum+=sum
   sign=-sign

print(f"Значение выражения {total_sum}")