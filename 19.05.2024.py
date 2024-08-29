import json
import csv
import pandas as pd
import requests

url = "https://jsonplaceholder.typicode.com/todos"
r = requests.get(url)
r.raise_for_status()
data = r.json()
with open('final.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
with open('final.json', 'r', encoding='UTF-8') as file_in:
    data_str = file_in.read()
print("Заголовок строки:", data_str[:100])
print('Конец строки:', data_str[-100:])

data_str = data_str.replace('true', 'True')
data_str = data_str.replace('false', 'False')
data_str = data_str.replace('null', 'None')
data_str = data_str.replace('\n', '')


def query_type(data):
    for ch in data:
        if ch == '{':
            return "dict"
        if ch == '[':
            return "list"
    return "value"


data_head = []


def get_json_head(data, loc=""):
    data = str(data)

    data_type = query_type(data)
    if data_type == "value":
        if loc[1:] not in data_head:
            data_head.append(loc[1:])
        return

    if data_type == "dict":
        data_dict = eval(data)
        for key in data_dict:
            get_json_head(data_dict[key], loc + "_" + key)
        return

    if data_type == "list":
        data_list = list(eval(data))
        for item in data_list:
            get_json_head(item, loc)
        return


get_json_head(data_str)
print(data_head[:10])
print(data_head[-10:])
print('Количество заголовков:', len(data_head))

data_head_dict = {}
for head in data_head:
    print(head)
    tmp = []
    for i in range(200):
        tmp.append("")
    data_head_dict[head] = tmp

for key in data_head[:10]:
    print(key, data_head_dict[key][:10])
    print(key, len(data_head_dict[key]))
    print(key, data_head_dict[key][:10], len(data_head_dict[key]))
    pass

row_now = 0


def get_json_table(data, loc="", rows=0):
    global row_now
    data = str(data)

    data_type = query_type(data)
    if data_type == "value":
        key = loc[1:]
        data_head_dict[key][rows] = data
        return

    if data_type == "dict":
        data_dict = eval(data)
        for key in data_dict:
            get_json_table(data_dict[key], loc + "_" + key, rows)
        return

    if data_type == "list":
        data_list = list(eval(data))
        for i in range(len(data_list)):
            if i > 0:
                row_now += 1
            get_json_table(data_list[i], loc, row_now)
        return


get_json_table(data_str)
for key in data_head[:10]:
    # print(key, data_head_dict[key][:10])
    # print(key, len(data_head_dict[key]))
    print(key, data_head_dict[key][:10], len(data_head_dict[key]))
    pass

with open('final_gbk.csv', 'w', encoding="gbk") as file_out:
    for head in data_head[:-1]:
        file_out.write(head)
        file_out.write(";")
    file_out.write(data_head[-1] + "\n")  # Последний разрыв строки
    for i in range(200):
        for head in data_head[:-1]:
            file_out.write(data_head_dict[head][i])
            file_out.write(";")
        last_key = data_head[-1]  # Взять последнюю голову
        file_out.write(data_head_dict[last_key][i])
        file_out.write("\n")

with open('final_utf8.csv', 'w', encoding="utf-8") as file_out:
    for head in data_head[:-1]:
        file_out.write(head)
        file_out.write(";")
    file_out.write(data_head[-1] + "\n")
    for i1 in range(200):
        for head in data_head[:-1]:
            file_out.write(data_head_dict[head][i])
            file_out.write(";")
        last_key = data_head[-1]
        file_out.write(data_head_dict[last_key][i])
        file_out.write("\n")

csv_data = pd.read_csv('final_utf8.csv')
csv_data.head(5)
