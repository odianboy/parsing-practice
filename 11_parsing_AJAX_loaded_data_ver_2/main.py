import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r


def get_page_data(response):
    if 'html' in response.headers['Content-Type']:
        html = response.text
    else:
        html = response.json()['content_html']

    soup = BeautifulSoup(html, 'lxml')

    items = soup.find_all('ytd-grid-video-renderer', class_='style-scope ytd-grid-renderer')

    for item in items:
        name = item.text.strip()
        url = item.find('a').get('href')


def main():
    url = 'https://www.youtube.com/c/%D0%A0%D0%B5%D0%B4%D0%B0%D0%BA%D1%86%D0%B8%D1%8F/videos'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
