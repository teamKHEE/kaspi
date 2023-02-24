import fake_useragent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import requests

class Main:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome('/home/xbtio/Downloads/chromedriver_linux64 (1)/chromedriver') # НУЖНО СКАЧАТЬ ДРАЙВЕР ЕСЛИ ИСПОЛЬЗУЕШЬ СЕЛЕНИУМ 
        self.wait = WebDriverWait(self.driver, 10)
        self.url_forNames= 'https://kaspi.kz/shop/nur-sultan/c/categories/?page='
        self.user = fake_useragent.UserAgent().random
        self.header = {'user-agent': self.user}

    def parseTheLinkForYernazar(self, item):
        link = item.find('a', 'item-card__name').get('href')
        self.driver.get(link)
        self.driver.implicitly_wait(10)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser') #Selenium usage 
        
        table = soup.find('td', class_='sellers-table__cell')
        link_item = table.find('a').get('href')
        return link_item
    
    def parseSellers_Info(self, link_item):
        link = f"https://kaspi.kz{link_item}"
        response = requests.get(link, headers=self.header)
        soup = BeautifulSoup(response.text,'lxml')
        name = soup.find('h1','merchant-profile__name').get_text()
        number = soup.find('span', 'merchant-profile__contact-text').get_text()
        return name,number


        
    def parseKaspi(self):
        page = 50000
        rresponce = requests.get(f'{self.url_forNames}{page}', headers=self.header)  
        soup = BeautifulSoup(rresponce.text, 'lxml')
        allProducts = soup.find_all('div', 'item-card__info')
        for item in allProducts:
            title = item.find('a', 'item-card__name').get_text()
            price = item.find('span','item-card__prices-price').get_text()
            link = item.find('a', 'item-card__name').get('href')
            linkForYernazar = self.parseTheLinkForYernazar(item)
            ll = self.parseSellers_Info(linkForYernazar)
            print(title, price, ll)
            


p = Main()

p.parseKaspi()



        
