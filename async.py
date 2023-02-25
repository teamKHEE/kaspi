import asyncio
import aiohttp
from bs4 import BeautifulSoup


class Main:
    def __init__(self) -> None:
        self.url_for_names = 'https://kaspi.kz/shop/nur-sultan/c/categories/?page='
        self.user = 'mozila'
        self.header = {'user-agent': self.user}

    async def parse_product(self, session, item):
        link = item.find('a', 'item-card__name').get('href')
        async with session.get(link) as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            try:
                table = soup.select_one('td.sellers-table__cell')
                link_item = table.find('a').get('href')
            except:
                link_item = '/shop/info/merchant/magnum/address-tab/?merchantId=Magnum'
            async with session.get(f"https://kaspi.kz{link_item}") as response:
                soup = BeautifulSoup(await response.text(), 'html.parser')
                name = soup.find('h1', 'merchant-profile__name').get_text()
                number = soup.find('span', 'merchant-profile__contact-text').get_text()
            return name, number

    async def parse_kaspi(self):
        page = 1
        i = 0

        async with aiohttp.ClientSession(headers=self.header) as session:
            while True:
                async with session.get(f'{self.url_for_names}{page}') as response:
                    soup = BeautifulSoup(await response.text(), 'html.parser')
                    all_products = soup.find_all('div', 'item-card__info')

                if not all_products:
                    break
                for item in all_products:
                    i +=1
                    title = item.find('a', 'item-card__name').get_text()
                    price = item.find('span', 'item-card__prices-price').get_text()
                    task = asyncio.ensure_future(self.parse_product(session, item))
                    name, number = await asyncio.wrap_future(task)
                    print(i, title, price, name, number)
                page += 1


p = Main()
asyncio.run(p.parse_kaspi())
