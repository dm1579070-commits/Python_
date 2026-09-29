import sys
print("Версия Питона: ", sys.version.split()[0])
print("Интерпритатор: ", sys.executable)

print("Кол-во путей поиска:", len(sys.path))
for q in sys.path[:4]:
    print("  ", q)

import math, random

print("math.pi =", math.pi)
print("random.random =", random.random())

mods=sorted(sys.modules)
print("Всего загружено модулей:", len(mods))
print("Пример:", mods[:5])

public = [n for n in dir(math) if not n.startswith('__')]
print("Публичных имен в math: ", len(public))
print ("Первые 8:", public [:8])

print ("Мой __name__=",__name__)
print ("Мой __file__=",__file__)

#вопрос 7)это для удобства: Питон смотрит в первую очередь на папку, где лежит файл. Опасность в том, что файл может "затемнить"\сломать реальный модуль и он не заработает
#вопрос 8) 1-импорт всех функций. 2 - только опр-ую функцию
#вопрос 9) Создала. Он найдет мой файл с функцией в названии. Питон попытается найти ее внутри. В итоге это приведет к "затемнению" реального кода
