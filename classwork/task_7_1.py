import sched, time

s = sched.scheduler(time.time, time.sleep)

def say(text):
    print(f"[{time.strftime("%H:%M:%S:")}]")

start = time.time()
print('Старт. Отсчет времени от t0 = 0\n')

s.enter(2, 1, say, ("Прошло 2 секунды (приоритет 1)",))
s.enter(2, 0, say, ("Прошло 2 секунды (приоритет 0 - сработает 1)",))
s.enter(1, 1, say, ("Прошло 1 секунда",))
s.enterabs(start + 3, 1, say, ("Абсолютное время t0+3 c",))
s.enter(0.5, 1, say, ("Прошло 0.5 секунды", ))

print("Очередь до run():", len(s.queue), "задач")

print("\nСодержиме s.queue")
print("run() блокирует поток, пока все задачи не выполнятся:\n")
for i, event in enumerate(s.queue):
  print(f"{i+1}. Время = {event[0]:.2f},Приоритет = {event[1]}, Действие {event[2]}:")
s.run()
print("\nГотово. пустая очередь?", s.empty())
#Вопросы:

#109)

#110)enterabs - запланировать на абсолютное время. enter - запланировать вызов через delay единиц времени.

#111)Ничего