from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
url = 'https://kaspi.kz/shop/p/magnum-luk-repchatyi-otbornyi-kazahstan-101349070/?c=750000000#!/item'
options = Options()
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.implicitly_wait(10)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
table = soup.find('table', class_='sellers-table__self')
if table:
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) > 1:
            name = cells[0].text.strip()
            value = cells[1].text.strip()
            print(name, value)
else:
    print("Table not found")

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# options = Options()
# driver = webdriver.Chrome(options=options)
# driver.get('https://kaspi.kz/shop/p/magnum-luk-repchatyi-otbornyi-kazahstan-101349070/?c=750000000#!/item')
# city_elem = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[data-city-id="710000000"]')))
# print(city_elem.is_displayed()) # True
# print(city_elem.is_enabled()) # True
# city_elem.click()
# print('Button clicked')
#
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'propTable')))
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# driver.quit()
# table = soup.find('table', class_='propTable')
# if table:
#     for row in table.find_all('tr'):
#         cells = row.find_all('td')
#         if len(cells) > 1:
#             name = cells[0].text.strip()
#             value = cells[1].text.strip()
#             print(name, value)
# else:
#     print("Table not found")

# import time
#
# from bs4 import BeautifulSoup
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select
#
#
# browser = webdriver.Chrome()
# browser.get("https://moodle.astanait.edu.kz")
# html_text = browser.page_source
# browser.find_element(By.XPATH, '//*[@id="page-wrapper"]/nav/ul[2]/li[2]/div/span/a').click()
# get_url = browser.current_url
# browser.get(get_url)
# browser.find_element(By.XPATH, '//*[@id="region-main"]/div/div[2]/div/div/div/div/div/div[2]/div[4]/div/a').click()
# get_url = browser.current_url
# browser.get(get_url)
# time.sleep(2)
# textbox = browser.find_element(By.XPATH, '//*[@id="i0116"]')
# textbox.send_keys('EMAIIIL')
#
# browser.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
# time.sleep(2)
# textbox = browser.find_element(By.XPATH, '//*[@id="i0118"]')
# textbox.send_keys("PASSWWOORRDD")
# browser.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
# time.sleep(2)
# browser.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()
#
# time.sleep(2)
# get_url = browser.current_url
# browser.get(get_url)
# browser.find_element(By.XPATH, '//*[@id="nav-drawer"]/nav/ul/li[6]/a').click()
#
# time.sleep(2)
# get_url = browser.current_url
# browser.get(get_url)
# browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/nav[1]/ul/li[4]/a').click()
#
# time.sleep(2)
# get_url = browser.current_url
# browser.get(get_url)
# output = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/section/div/table/tbody/tr[3]/td[2]').text
# print(output)
#
#
# while(True):
#     pass
#
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
#
#
# class Parse:
#     def __init__(self) -> None:
#         options = Options()
#         self.driver = webdriver.Chrome(options=options)
#         self.wait = WebDriverWait(self.driver, 10)
#
#     def getGrades(self, link):
#         self.driver.get(link)
#         soup = BeautifulSoup(self.driver.page_source)
#         regMid = soup.find_all('td', class_='column-grade')
#         values = {'Register Term': regMid[2].get_text(), 'Register Final': regMid[3].get_text()}
#         return values
#
#     def message(self, q, a):
#         return '{0} \nRegister Term  : {1} \nRegister Final : {2}'.format(q, a['Register Term'], a['Register Final'])
#
#     def parse(self, log, pas):
#         self.driver.get('https://moodle.astanait.edu.kz/login/index.php')
#
#         element1 = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'OpenID Connect')))
#         element1.click()
#
#         login = self.wait.until(EC.visibility_of_element_located((By.ID, "i0116"))).send_keys(log + '@astanait.edu.kz')
#
#         button = self.wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
#         button = self.wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
#
#         passw = self.wait.until(EC.visibility_of_element_located((By.ID, "i0118"))).send_keys(pas)
#
#         button = self.wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
#         button = self.wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
#
#         button = self.wait.until(EC.element_to_be_clickable((By.ID, "idBtn_Back")))
#         button = self.wait.until(EC.element_to_be_clickable((By.ID, "idBtn_Back"))).click()
#
#         self.driver.get('https://moodle.astanait.edu.kz/grade/report/overview/index.php')
#
#         listOfNames = []
#
#         soup = BeautifulSoup(self.driver.page_source, 'html.parser')
#         for link in soup.find_all('td'):
#             if link.attrs['class'][1] == 'c0' and link.find('a'):
#                 listOfNames.append((link.find('a').get_text(), self.getGrades(link.find('a').get('href'))))
#
#         self.driver.get('https://moodle.astanait.edu.kz/login/logout.php?sesskey=h8SqwJrWsa')
#         button1 = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))).click()
#         self.driver.close()
#         return dict(listOfNames)
#
#
# parser = Parse()
# result = parser.parse('220268', '3YxACiJK3PdU9w8')
# print(result)
