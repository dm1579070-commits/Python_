import sys, site

print("Исполняемый файл:", sys.executable)
print("Преыикс     :", sys.prefix)
print("Базовый префикс:", sys.base_prefix)
print("В виртуальном окружении ?", sys.prefix != sys.base_prefix)
print("site-packages :", site.getsitepackages())

#Вопросы:

# 83) Активирует окружение. deactivate не удаляет пакеты потому что он просто переключает пространство в преждний нейтральный режим

# 84)

# 85)Команды начнут работать некорректно. Переменная PATH запутается
