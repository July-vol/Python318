# Обмен местами двух строк в файле
# Тест:
# Замена строки в текстовом файле;
# Изменить строку в списке;
# Записать список в файл;
#
# pos1 =1
# pos2 = 2
# Замена строки в текстовой файле;
# записать список в файл;
# изменить строку в списке;


file = "text2.txt"

f = open(file, "w")
f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
f.close()

f = open(file, 'r')
read_line = f.readlines()
f.close()

print(read_line)
pos1 = int(input("pos1 = "))
pos2 = int(input("pos2 = "))
if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):  # a, b = b, a
    read_line[pos1], read_line[pos2] = read_line[pos2], read_line[pos1]
else:
    print("Такой строки нет")
print(read_line)

f = open(file, "w")
f.writelines(read_line)
f.close()
