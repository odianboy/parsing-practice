import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p = soup.find('header', id='masthead').find('div').find('p').text

    return p


def main():
    url = 'https://ru.wordpress.org/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
