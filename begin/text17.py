a= float (input ("точка a: "))
b= float (input ("точка b : "))
c= float (input ("точка c: "))
d_AC=abs(c-a)
d_BC=abs(c-b)
amount=d_AC+d_BC
print("Длина отрезка AC: ", d_AC)
print("Длина отрезка BC: ", d_BC)
print("Сумма отрезков AC и BC: ", amount)