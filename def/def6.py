def DigitCountSum(K):
    Count=0
    Sum=0
    for i in str(K):
     Count+=1
     Sum+=int(i)
    return Count, Sum

print(DigitCountSum(1234567)) 