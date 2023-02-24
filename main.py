import fake_useragent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests

user = fake_useragent.UserAgent().random

header = {'user-agent': user}
url_forNames= 'https://kaspi.kz/shop/nur-sultan/c/categories/?page='
counter = 1
for i in range(5):
    rresponce = requests.get(f"{url_forNames}{counter}", headers=header)
    soup = BeautifulSoup(rresponce.text, 'lxml')
    block = soup.find_all('div', 'item-card__info')
    for item in block:
        title = item.find('a', 'item-card__name').get_text()
        price = item.find('span','item-card__prices-price').get_text()
        link = item.find('a', 'item-card__name').get('href')
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        driver.implicitly_wait(10)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        table = soup.find('td', class_='sellers-table__cell')
        link_item = table.find('a').get('href')
        print(title, price, link_item)
    counter += 1
