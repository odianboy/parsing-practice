import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)

    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((
            data['name'],
            data['url'],
            data['price']
        ))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table', class_='h7vnx2-2_parsing_multiple_data czTsgW cmc-table').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')

        try:
            name = tds[2].find('p').text.strip()
        except:
            name = ''
        try:
            url = 'https://coinmarketcap.com' + tds[2].find('a').get('href')
        except:
            url = ''
        try:
            price = tds[3].find('a', class_='cmc-link').text
        except:
            price = ''

        data = {
            'name': name,
            'url': url,
            'price': price
        }

        write_csv(data)


def main():
    pattern = 'https://coinmarketcap.com/?page={}'

    for i in range(1, 7):
        url = pattern.format(str(i))
        get_page_data(get_html(url))


if __name__ == '__main__':
    main()
