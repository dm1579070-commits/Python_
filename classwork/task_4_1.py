import six
print ("six.__version__=", six.__version__)
print("six.__file__", six.__file__)

print("PY2?", six.PY2, "| PY3?", six.PY3)
print("six.path[0] =", sys.path[0])

import sys
print("sys.path[0] =", sys.path[0])

import site
("site-packages:", site.getsitepackages())

#Вопросы:

#57)pip = Устанавливает пакеты в то окружение, которому принадлежит. Если вирт. окр-ие не доступно - то в глоб. Python.
#  -m pip = Для текущего Python, указывает на явно, какой интерпретатор использовать.

#58)Requires - зависимости самого пакета. Requyred-by = кто зависит от этого пакета

#59)Потому что pip удаляет только свои файлы (.py), а __pycache__ создает сам Python 