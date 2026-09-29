n = int (input("Число N(>0): ")) 
ATM= 1.0
for i in range (1, n+1):
    w=(i/10) + 1
    ATM *= w
print ("Произведение: ", ATM)