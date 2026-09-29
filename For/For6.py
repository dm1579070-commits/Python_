prise = float(input("Цена 1 кг конфет: "))
for kg in range(12, 21, 2):
    weight=kg/10
    cost=prise*weight
    print(f"Цена за {weight} кг конфет: ", cost)