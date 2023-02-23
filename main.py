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
