from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

yandex_url = 'https://yandex.ru/pogoda/details/10-day-weather?lat=58.635513&lon=59.79863&via=ms'
ua = UserAgent()
headers = {
    'accept': '*/*',
    'User-Agent': ua.random,
}


def html_to_text(url=yandex_url):
    return requests.get(url, headers=headers).content

def save_file(text):
    with open('temp.html', 'wb') as f:
        f.write(text)


if __name__ == '__main__':
    soup = BeautifulSoup(html_to_text(), 'lxml')
    save_file(soup.contents)
