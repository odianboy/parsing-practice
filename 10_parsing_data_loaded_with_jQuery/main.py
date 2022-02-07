import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    user_agent = {'User-Agent': 'Mozilla/5_writing_data_csv_files.0 (Windows NT 10_parsing_data_loaded_with_jQuery.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/95.0.4638.69 Safari/537.36'}
    r = requests.get(url, headers=user_agent)
    return r.text


def write_csv(data):
    with open('testimonials.csv', 'a') as file:
        order = ['author', 'since']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


def get_articles(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', class_='testimonial-container').find_all('article')

    return ts   # [] or [a, d, c]


def get_page_data(ts):
    for t in ts:
        try:
            since = t.find('p', class_='traxer-since').text.strip()
        except:
            since = ''
        try:
            author = t.find('p', class_='testimonial-author').text.strip()
        except:
            author = ''
        data = {
            'author': author,
            'since': since
        }
        write_csv(data)


def main():

    """
        1. Получение контейнера с отзывами и списка с отзывами
        2. Если спаисок есть, то парсим отзывы
        3. Если список пустой, то список прерывается
    """

    while True:
        page = 1
        url = 'https://catertrax.com/why-catertrax/traxers/page/{}/?themify_builder_infinite_scroll=yes'\
            .format(str(page))

        articles = get_articles(get_html(url))  # [] or [1_basic_example, 2_parsing_multiple_data, 3_parsing_tabular_data]

        if articles:
            get_page_data(articles)
            page += 1
        else:
            break


if __name__ == '__main__':
    main()
