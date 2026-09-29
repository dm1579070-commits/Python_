a=float(input("число A (>1)): "))
count=0.0
k=1
while count+1/k<a:
    count+=1/k  
    k+=1
w=k-1
print(f"наибольшее из чисел К: {w}")
print(f"сумма ряда К: {count}")