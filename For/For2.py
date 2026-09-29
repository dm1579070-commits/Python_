a = int(input("Введите A: "))
b = int(input("Введите B: "))
count=0

if a<b:
    for i in range(a, b + 1):
        print(i)
        count+=1


    print("Кол-во чисел: ", count)
    
else:
    print("Не соответствует условию задачи")