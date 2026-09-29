n = int(input("Число N(>0): "))
ATM= 0
for i in range(n, 2* n+1):
    w=i**2
    ATM += w
print ("Сумма: ", ATM)