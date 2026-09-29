a = int(input("Введите A(Меньше числа B): "))
b = int(input("Введите B(Больше числа А): "))
ATM=1
for i in range(a, b+1):
    ATM*=i
print(f"Произведение всех целых чисел {ATM}")
