A1 = float(input("Коэффицент A1: "))
B1 = float(input("Коэффицент B1: "))
C1 = float(input("Коэффицент C1: "))
A2 = float(input("Коэффицент A2: "))
B2 = float(input("Коэффицент B2: "))
C2 = float(input("Коэффицент C2: "))
D= A1*B2-A2*B1
x=(C1*B2-C2*B1)/D
y=(A1*C2-A2*C1)/D
print(f"Решение системы линейных уравнений: x={x}, y={y}" )