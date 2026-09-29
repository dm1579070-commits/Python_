a = int(input("Введите A(Меньше числа B): "))
b = int(input("Введите B(Больше числа А): "))
ATM=0
for i in range(a, b+1):
    ATM+=i
print(f"Сумма всех целых чисел {ATM}")
