X=float(input("Вещественное число( |x|<1 ): ")) #Проверить потом (+)
N=int(input("Целое число (N>0): "))
total_sum=X
factorial_1=1.0 #Для числителя
factorial_2=1.0 #Для знаменателя
for i in range(1,N+1):
   a1=2*i-1  #по типу числитель
   factorial_1*=a1 #Для числителя
   c=2*i+1 #СТЕПЕНЬ Х
   w=X**c 
   a2=(2*i)*(2*i+1)  #знаменатель
   factorial_2*=a2 #Для знаменателя
   sum= factorial_1 * w/factorial_2  #Итог
   total_sum+=sum

print(f"Значение выражения {total_sum}")