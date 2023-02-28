from bs4 import BeautifulSoup

import fake_useragent
import requests


class Product:
    title = 'No title'
    price = "No price"
    description = 'No description'
    product_url = ''
    seller = 'No seller'
    phone_number = 'No number'
    output = {
        'title': title,
        'price': price,
        'description': description
    }

    def __init__(self) -> None:
        self.kaspi_kz = 'https://kaspi.kz/shop/nur-sultan/c/categories/?page='
        self.user = fake_useragent.UserAgent().random
        self.header = {'user-agent': self.user}

    def parseProduct(self, page) -> list: # returns a list of dictionaries
        i = 0
        temp_list = []

        response = requests.get(
            f"{self.kaspi_kz}{page}", headers=self.header)
        soup = BeautifulSoup(response.text, 'lxml')
        allProducts = soup.find_all('div', 'item-card__info')

        for item in allProducts:
            i += 1
            temp = item.find('a', 'item-card__name')
            new_url = temp.get('href')
            title = temp.get_text()
            price = item.find('span', 'item-card__prices-price').get_text()
            # Дескришн через реквестс
            link_desc = requests.get(new_url, headers=self.header)
            soup = BeautifulSoup(link_desc.text, 'lxml')
            description = soup.find(
                'div', 'item__description-text').get_text()
            # Редачим строки
            price = price.replace('\n', '').strip().replace(
                '₸', '').replace(' ', '')
            title = title.replace('\n', '').strip().replace('\t', '')
            description = description.replace(
                '\n', '').strip().replace("  ", '').strip()
            temp_list.append({'id': i, 'title': title, 'price': int(
                price), 'description': description, 'link_product': new_url})
        #parses 12 items in one page 
        return temp_list



