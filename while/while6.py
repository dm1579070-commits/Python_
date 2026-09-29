
n=int(input("число N): "))
count=1.0
while n>0:
   count*=n
   n-=2

print(f"Двойной факториал: {count}")