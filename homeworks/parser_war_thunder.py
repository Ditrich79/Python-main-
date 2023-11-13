from bs4 import BeautifulSoup
import requests


def get_html(url):
    result = requests.get(url)
    return result.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find_all('div', class_='tree-item-text')
    lst = []
    for plugin in p1:
        name = plugin.find('span').text.lstrip('▂')
        name2 = name + '\n'
        lst.append(name2)
        with open(r'F:\Учёба Python\tanks.txt', 'w', encoding='utf-8') as file:
            file.writelines(lst)


def main():
    url = 'https://wiki.warthunder.ru/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%9D%D0%B0%D0%B7%D0%B5%D0%BC%D0%BD%D0%B0%D1%8F_%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B0_%D0%A1%D0%A1%D0%A1%D0%A0'
    get_data(get_html(url))


if __name__ == '__main__':
    main()

