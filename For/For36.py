k = int(input("Введите K (степень) (k>0) "))
n = int(input("Введите N (целое число) (N>0)"))
total_sum=0.0
for i in range(1, n+1):
    w=i**k
    total_sum+=w


print(f"Cумма: {total_sum}")