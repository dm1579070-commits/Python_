N=int(input("число(>0)): "))
is_prime=True
i=2
while i<N:
   if N % i == 0:
     is_prime=False
   i+=1

print(is_prime)