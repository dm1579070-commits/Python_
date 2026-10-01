import random
deck = [f"{v}{s}" for s in "SHDS" for v in "6789TJQKA"]
random.seed(7)
print("Всего карт в колоде: ", len(deck))

hand = random.sample(deck, 5)
print ("Ручка игрока (sample):", hand)

print("Карта дня (choice)    :", random.choice(deck))

weights = {"обычная": 70, "редкая": 25, "легендарная": 5}
loot = random.choices(list(weights), weights=list(weights.values()), k=5)
print("Лут (choices, 5 шт.):", loot)

random.shuffle(deck)
print("После shuffle       :", deck[:6], "...")

print("\n--- Раздача 3 игрокам по 5 карт ---")
players = ["Алиса", "Борис", "Вера"]
pool = deck.copy()
for p in players:
    hand = random.sample(pool, 5)
    print(f"{p:6s}: {hand}")
    for i in hand:
     pool.remove(i)

#Вопросы:

#39)choices()- выбирает k элементов с возвращением (могут повторяться). sample()- k элементов без возвращения (уникальные)

#40) Произойдет ошибка ValueError, потому что в колоде всего 36 карт, а sample не может выбрать 40 элементов из 36 возможных

#41)Потому что shuffle()- меняет список на месте и возвращает None. A sorted  создает и возвращает новый список, не изменяя исходный
