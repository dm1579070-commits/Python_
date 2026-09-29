N=int(input("Челое число(>0)): "))
count=0
while N>0:
    digh=N % 10
    count=count*10+digh
    N=N//10

print(count)