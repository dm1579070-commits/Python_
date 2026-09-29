n = int(input("Введите N (целое число) (N>0)")) #НЕ ДОДЕЛАНО
total_sum=0.0
for i in range(1, n+1):  #для основания
    degee=n-i+1
    w=i**degee
    total_sum+=w

print(f"Cумма : {total_sum}")