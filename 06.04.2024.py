# Напишите программу, которая просканирует выбранную директорию
# и для всех ее объектов выведет следующую информацию на экран:
# имя -тип- размер (только для фйлов)
# * тип объектов: файл, директория
# * размер: только для файлов
#
# project.txt - file - 658 bytes
# test - dir
# test.txt - file -830 bytes
# test1 - dir

import os

dir_name = "nested1"

objs = os.listdir(dir_name)
print(objs)

for obj in objs:
    p = os.path.join(dir_name, obj)
    # print(p)
    if os.path.isfile(p):
        print(f"{obj} - file - {os.path.getsize(p)} bytes")
    elif os.path.isdir(p):
        print(f"{obj} - dir")
