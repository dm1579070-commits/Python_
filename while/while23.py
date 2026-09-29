A=int(input("число A: "))
B=int(input("число B: "))
while B!=0:
   A, B= B,A % B

print(A)