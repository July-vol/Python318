# Домашнее задание: Реализовать парсинг данных из любого интернет ресурса с однотипными данными
# и сохранить их в формате csv

import csv

import requests
from bs4 import BeautifulSoup


def main():
    for i in range(2, 3):
        url = "https://mobile71.ru/novyie-telefonyi/novyie-telefonyi-xiaomi.html?yclid=15357660547446472703"
        get_data(get_html(url))


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open("new_phones.csv", "a") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\r")
        writer.writerow((data['image'], data['name'], data['tech'], data['price']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all("div", class_="item")
    for el in elements:
        try:
            image = el.find("div", class_="image")
        except AttributeError:
            image = ""

        try:
            name = el.find("div", class_="name").text
        except AttributeError:
            name = ""

        try:
            tech = el.find("div", class_="tech").text.strip

        except AttributeError:
            tech = ""

        try:
            price = el.find("div", class_="price").text.strip
        except AttributeError:
            price = ""

        data = {
            'image': image,
            'name': name,
            'tech': tech,
            'price': price
        }
        write_csv(data)


if __name__ == '__main__':
    main()
