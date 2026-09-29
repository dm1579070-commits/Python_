prise = float(input("Цена 1 кг конфет: "))
for kg in range(1,10+1):
    weight=kg/10
    self=prise*weight
    print(f"Цена за {weight} кг конфет: ", self)