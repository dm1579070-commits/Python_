X=float(input("Вещественное число( |x|<1 ): ")) #Проверить потом (+)
N=int(input("Целое число (N>0): "))
total_sum=1.0
factorial_1=1.0 #Для числителя
factorial_2=1.0 #Для знаменателя
sign=1
for i in range(1,N+1):
   a1=abs(2*i-3)  #по типу числитель
   factorial_1*=a1 #Для числителя
   w=X**i #СТЕПЕНЬ Х
   a2=2*i  #знаменатель
   factorial_2*=a2 #Для знаменателя
   suma= sign*(factorial_1 * w /factorial_2)  #Итог
   total_sum+=suma
   sign=-sign

print(f"Значение выражения {total_sum}")