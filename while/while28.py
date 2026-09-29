e=float(input("число N: "))
A1=2.0
k=2
A2= 2+1 / A1
while abs(A2-A1)>=e:
    A1=A2
    A2= 2+1/ A1
    k+=1

print(k, A1, A2)