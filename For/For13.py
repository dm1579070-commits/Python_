n = int(input("N слагаемых (N>0): "))
ATM= 0.0
sign=1
for i in range(1,n+1):
    w=1.0/i
    ATM+=sign*w
    sign=-sign
print ("Сумма: ", ATM)