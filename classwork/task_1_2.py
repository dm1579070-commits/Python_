import mymodule
from mymodule import circle_area, VERSION 
from mymodule import circle_len as perimeter
import mymodule as mm

print("1) mymodule.circle_area(5) =", mymodule.circle_area (5))
print("2) circle_area(5)          =", circle_area(5))
print("3) perimeter(5)            =", perimeter (5))
print("4) mm.PI                   =", mm.PI)

print("dir(mymodule) ->", [n for n in dir(mymodule) if not n.startswith('__')])
print("mymodule.__name__=", mymodule.__name__)
print(__name__) # номер 17
print("mymodule.__file__=", mymodule.__file__)
#Работает, потому что сам доступ к ней не запрещен, но ипользуется для внутренней работы модуля.
# Если надо - программист может вывести эту переменную
print("mm._helper() =", mm._helper()) 

#Ответы на вопросы:
#15)Это позволяет хранить в модуле и полезные функции, и самопроверку (только когда файл запущен как программа)
#16)засоряет пространство имён и делает код непрозрачным
#17)__main__

