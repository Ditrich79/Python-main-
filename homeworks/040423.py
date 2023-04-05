import requests
from bs4 import BeautifulSoup


def get_html(url):
    res = requests.get(url)
    return res.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find_all("div", class_="item-title 21")
    for plugin in p1:
        name = plugin.find("span").text
        print(name)
    p2 = soup.find_all("div", class_="item_info main_item_wrapper TYPE_1")
    for plugin in p2:
        price = plugin.find("button")["data-price"]
        description = plugin.find("button")["data-text"].strip()
        print(description)
        print(price)
    p3 = soup.find_all("div", class_="brand")
    for plugin in p3:
        manufacturer = plugin.text.strip()
        print(manufacturer)


def main():
    url = "https://svet161.ru/catalog/svetilniki/podvesnye/"
    get_data(get_html(url))


if __name__ == '__main__':
    main()


