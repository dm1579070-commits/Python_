a=int(input("число A (меньше B): "))
b=int(input("Целое число B (больше А): "))
for i in range(a, b+1):

    for j in range(i):
       print(i, end =" ")
    print()