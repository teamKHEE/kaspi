import fake_useragent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


from requests_html import HTMLSession


import requests


class Main:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        self.url_forNames = 'https://kaspi.kz/shop/nur-sultan/c/categories/?page='
        self.user = fake_useragent.UserAgent().random
        self.header = {'user-agent': self.user}
        self.boooo = False

    def parseTheLinkForYernazar(self, item):
        link = item.find('a', 'item-card__name').get('href')
        self.driver.get(link)
        self.driver.implicitly_wait(10)
        if (self.boooo == False):
            self.wait.until(EC.element_to_be_clickable((
                By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/div[2]'))).click()
            self.boooo = True
        soup = BeautifulSoup(self.driver.page_source,
                             'lxml')
        try:  # Selenium usage
            table = soup.find('td', class_='sellers-table__cell')
            link_item = table.find('a').get('href')
            return link_item
        except:
            link_item = '/shop/info/merchant/magnum/address-tab/?merchantId=Magnum'
            return link_item

    def parseSellers_Info(self, link_item):
        link = f"https://kaspi.kz{link_item}"
        response = requests.get(link, headers=self.header)
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find('h1', 'merchant-profile__name').get_text()
        number = soup.find('span', 'merchant-profile__contact-text').get_text()
        return name, number

    def parseKaspi(self):
        page = 1
        i = 0

        while True:
            rresponce = requests.get(
                f'{self.url_forNames}{page}', headers=self.header)
            soup = BeautifulSoup(rresponce.text, 'lxml')
            allProducts = soup.find_all('div', 'item-card__info')

            if not allProducts:
                break
            for item in allProducts:
                i = i + 1
                title = item.find('a', 'item-card__name').get_text()
                price = item.find('span', 'item-card__prices-price').get_text()
                link = item.find('a', 'item-card__name').get('href')
                linkForYernazar = self.parseTheLinkForYernazar(item)
                ll = self.parseSellers_Info(linkForYernazar)
                print(i, title, price, ll)
            page += 1


p = Main()

p.parseKaspi()
