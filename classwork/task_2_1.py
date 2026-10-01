import random
random.seed(42)
print("random()              :", round (random.random(), 6))
print("uniform(1, 10)        :", round(random.uniform(1, 10), 3))
print("randint(1, 6)         :", random.randint(1, 6))
print("randrange(0, 100, 5)  :", random.randrange(0, 100, 5))

print("\n--- Бросок двух кубиков, 5 раз ---")
for i in range(1, 6):
    a, b = random.randint(1, 6), random.randint(1, 6)
    print(f"Бросок {i}: {a} + {b} = {a + b}")

print("\n--- Статистика 10 000 бросков одного кубика ---")
random.seed(2026)
counts = {i: 0 for i in range(1, 7)}
N=10_000
for i in range(N):
    counts[random.randint(1, 6)] += 1

for face, cnt in sorted(counts.items()):
    bar = "#" * (cnt // 50)
    procent = cnt / N *100
    proc2 = procent -16.67
    print(f"{face}: {cnt:5d}  ({cnt / N * 100:5.2f}%)   {bar}")
    print(f"Отклонение =  {proc2:+.2f}")

#Вопросы:

#31)Нет, не являются. Это псевдослучайные числа на алгоритме Мерсенна-твистер. 
# Функция Seed() помогает генератору выдавать абсолютно одинаковую последовательность чисел и делать случайность значений - управляемой.

#32)Потому что работает статистическая погрешность - всегда есть небольшие отклонения.

#33) secrets. Random () не подходит для криптографии