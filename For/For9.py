a = int(input("Введите A(Меньше числа B): "))
b = int(input("Введите B(Больше числа А): "))
ATM=0
if a<b:
   for i in range(a, b+1):
        ATM+=i**2
    
print(f"Сумма всех целых чисел в квадрате {ATM}")