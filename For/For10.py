n = int(input("Число N: ")) 
ATM= 0
for i in range(1, n+1):
    w=1/i
    ATM += w

print ("Сумма: ", ATM)