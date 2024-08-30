import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        news = self.html.find_all("div", class_="col-md-4 col-sm-6 archives__item")
        for item in news:
            title = item.find("h1").text
            href = item.find('a').get('href')
            image = item.find("div", class_="singlenew__img")
            self.res.append({
                "title": title,
                "href": href,
                "image": image
            })

    def save(self):
        with open(self.path, "w") as f:
            i = 1
            for item in self.res:
                f.write(f"Новость № {i}\n\nНазвание: {item['title']}\nСсылка: {item['href']}\nФото: "
                        f"{item['image']}\n\n{'*' * 40}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
