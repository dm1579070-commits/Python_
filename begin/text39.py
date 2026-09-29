A = float(input("Коэффицент A: "))
B = float(input("Коэффицент B: "))
C = float(input("Коэффицент C: "))
D=B**2-4*A*C
if not A==0 and D<=0:
    x1=(-B+D*0.5)/(2*A)
    x2=(-B-D*0.5)/(2*A)
    bolshee = max(x1, x2)
    menshee = min(x1, x2)
    print("Корни равны: ", bolshee, menshee)
else:
    print("Условия задачи не соблюдены")