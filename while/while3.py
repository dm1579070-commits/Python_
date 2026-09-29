n=int(input("число N: "))
k=int(input("Целое число K: "))
count=0
while n >= k:
    n=n-k
    count+=1
print(f"Частное от деления нацело N на K={count}")
print(f" остаток от деления нацело N на K={n}")