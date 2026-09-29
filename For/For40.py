a=int(input("число A (меньше B): "))
b=int(input("Целое число B (больше А): "))
suma=1
for i in range(a, b+1):

    for j in range(suma):
       print(i, end =" ")
    print()

    suma+=1