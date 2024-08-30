# Спарсить данные с нескольких страниц любого интернет ресурса
# с использованием объектно-ориентированного подхода

import requests
from bs4 import BeautifulSoup
from ParsersPars import Parser


def main():
    pars = Parser('https://apnegg.ru/news_category/novosti/?yclid=6056363783713456127', "n4.txt")
    pars.run()


if __name__ == '__main__':
    main()
