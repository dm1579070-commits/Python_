n=int(input("число N (степень числа 3(>0)): "))

while n % 3 == 0:
   n=n//3


if n==1:
      print (True)
else:
      print(False)