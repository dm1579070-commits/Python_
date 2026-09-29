a=int(input("число A (больше B) - это 1 большой отрезок: "))
b=int(input("Целое число B (меньше А)-  длина отрезка B: "))
count=0
while count+b <= a:
    count+=b
w=a-count
print(f"Длина не занятой части отрезка А ={w}")
    