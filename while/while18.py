N=int(input("Челое число(>0)): "))
count=0
summa=0
while N>0:
    digh=N % 10
    count+=1
    summa+=digh
    N=N//10
print(count, summa)