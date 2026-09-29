N=int(input("Челое число(>0)): "))
has_two=False
while N>0:
    digh=N % 10
    if digh % 2!=0:
      has_two=True
    N=N//10

print(has_two)