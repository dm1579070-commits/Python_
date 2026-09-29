P=float(input("Процент длины пробега(0<P<50)): "))
S=10.0
K=1
total=10
while total<200:
    S+=((S*P)/100)
    total+=S
    K+=1
print(f"Через сколько дней: {K}")
print(f"Сумарный пробег: {total}")