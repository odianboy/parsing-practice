from bs4 import BeautifulSoup
import re

""" 
    .find() - метод
    .find_all() - метод

    .parent - свойство
    .find_parent() - метод

    .parents
    .find_parents()

    .find_next_siblibg()
    .find_previous_sibling()

"""


def get_copywriter(tag):
    whois = tag.find('div', id='whois').text.strip()

    if 'Copywriter'in whois:
        return tag
    return None


def get_salary(s):
    # salary: 2700 usd per month
    pattern = r'\d{1_basic_example,9_parsing_data_into_multiple_processes}'
    # salary = re.findall(pattern, s)[0]
    salary = re.search(pattern, s).group()
    print(salary)


def main():
    file = open('index.html').read()
    soup = BeautifulSoup(file, 'lxml')

    """
        row = soup.find_all('div', {'data-set': 'salary'})
    
        alena = soup.find('div', text='Alena').find_parent(class_='row')
    
        print(alena)
    
        copywrites = []
        persons = soup.find_all('div', class_='row')
    
        for person in persons:
            cw = get_copywriter(person)
            if cw:
                copywrites.append(cw)
        print(copywrites)
    
    """

    salary = soup.find_all('div', {'data-set': 'salary'})

    for i in salary:
        get_salary(i.text)

    """
        регулярные выржания
    
        ^ - начало строки
        $ - конец строки
        . - любой символ
        + - неограничное кол-во вхождений
        '\d' - цифра
        '\w' - буквы, цифры, _
    
        @twitter
    
        ^@\w+
    
    """


if __name__ == '__main__':
    main()
