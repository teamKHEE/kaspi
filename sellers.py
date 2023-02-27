from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import fake_useragent
import requests
import time


class Seller:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.url_forNames = 'https://kaspi.kz/shop/nur-sultan/c/categories/?page='
        self.user = fake_useragent.UserAgent().random
        self.header = {'user-agent': self.user}

    def find_td(self, link):
        self.driver.get(link)
        time.sleep(3)
        self.driver.implicitly_wait(10)

        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        if soup.find('td', class_='sellers-table__cell') != None:
            table = soup.find('td', class_='sellers-table__cell')
            link_item = table.find('a').get('href')
            return link_item
        else:
            return "No Info"

    def parseSellers(self, seller_link) -> list:
        if seller_link == "No Info":
            return ["No Info", "No Info"]
        response = requests.get(
            f"https://kaspi.kz{seller_link}", headers=self.header)
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find('h1', 'merchant-profile__name').get_text()
        number = soup.find('span', 'merchant-profile__contact-text').get_text()
        return [name, number]

    def drugSellers(self, links) -> list:
        seller_info = []
        for link in links:
            seller_link = self.find_td(str(link[0]))
            # print(seller_link)
            seller_info.append(self.parseSellers(seller_link))
        return seller_info
