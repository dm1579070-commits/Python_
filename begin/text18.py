a= float (input ("точкa a: "))
c= float (input ("точкa c: "))
b= float (input ("точka b: "))
if a<c<b or b<c<a:
 Final=abs(c-a) * abs(b-c)
 print ("Произведение длин: ", Final)
else:
 print("Пшел, чмо, введи нормально. Точка c посередине ")