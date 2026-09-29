x1= float (input ("точкa x1: "))
y1= float (input ("точкa y1: "))
x2= float (input ("точкa x2: "))
y2= float (input ("точкa y2: "))
x3= float (input ("точкa x3: "))
y3= float (input ("точкa y3: "))
a=((x2-x1)**2+(y2-y1)**2)*0,5
b=((x3-x2)**2+(y3-y2)**2)*0,5
c=((x3-x1)**2+(y3-y1)**2)*0,5
p=float(a+b+c)/2
S=(p*(p-a)(p-b)(p-c))*0.5
P=a+b+c
print("Периметр", P)
print('Площадь ', S)