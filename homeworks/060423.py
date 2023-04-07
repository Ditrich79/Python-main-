import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    result = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        base = self.html.find_all("div", class_="card_info")
        for plugin in base:
            names = plugin.find("div", class_="book_name").text
            description = plugin.find("div", class_="dscr").text
            author = plugin.find("a", class_="genre").text
            rating = plugin.find("div", class_="rating_count").text
            self.result.append({
                'names': names,
                'description': description,
                'author': author,
                'rating': rating
            })

    def run(self):
        self.get_html()
        self.parsing()
        self.save()

    def save(self):
        with open(self.path, 'w') as f:
            i = 1
            for item in self.result:
                f.write(f"Книга № {i}\n\nНазвание: {item['names']}\n{'-' * 70}\nАвтор: {item['author']}\n{'-' * 70}\n"
                        f"Описание: {item['description']}\n{'-' * 70}\nРейтинг: {item['rating']}\n\n{'*' * 70}\n")
                i += 1


def main():
    for i in range(0, 3):
        pars = Parser(f'https://avidreaders.ru/books/{i}', 'books2.txt')
        pars.run()


if __name__ == '__main__':
    main()



