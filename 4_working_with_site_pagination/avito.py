import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)

    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f)
        pass


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    divs = soup.find(
        'div', class_='items-items-kAJAg').find_all(
        'div',
        class_='iva-item-root-Nj_hb photo-slider-slider-_PvpN iva-item-list-H_dpX iva-item-redesign-nV4C4 '
               'iva-item-responsive-gIKjW items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')

    for div in divs:
        try:
            name = div.find('a',
                            class_='link-link-MbQDP link-design-default-_nSbv title-root-j7cja iva-item-title-_qCwt '
                                   'title-listRedesign-XHq38 title-root_maxHeight-SXHes').text
        except:
            name = ''
            print(divs)


def main():
    url = 'https://www.avito.ru/tihoretsk/bytovaya_elektronika'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
