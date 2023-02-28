import psycopg2
from product_info import Product
from sellers import Seller


class FillDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            user="test",
            password="thyfh123",
            host="localhost",
            port="5432",
            database="mydb")
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)

    def close(self):
        self.cur.close()
        self.conn.close()

    def fill_db_with_product(self):
        parse = Product()
        page = 1425
        while True:
            p = parse.parseProduct(page)
            for i in range(12):
                postgres_insert_query = """INSERT INTO "bforabzal"(title, price, description, link_product, seller, phone_number) VALUES(%s, %s, %s, %s, %s, %s)"""
                title = p[i]['title']
                price = p[i]['price']
                description = p[i]['description']
                link_product = p[i]['link_product']
                seller = Seller().parseSellers(link_product)
                record_to_insert = (title, price, description, link_product, seller[0], seller[1])
                self.cur.execute(postgres_insert_query, record_to_insert)
                self.conn.commit()
                print(f"Page {page}, index={i}. successfully inserted ")
            page += 1

    def get_url_link(self) -> list:
        select_query = """SELECT link_product FROM "bForAbzal" """
        self.cur.execute(select_query)
        result = self.cur.fetchall()
        test = Seller()
        ll = test.drugSellers(list(result))
        return ll

    def fill_db_with_seller(self):
        wow = self.get_url_link()
        for t, n in wow:
            postgres_insert_query = """INSERT INTO "attempt_at_22:47"(drug_seller, their_contacts) VALUES(%s, %s) """
            record_to_insert = (str(t), str(n))
            self.cur.execute(postgres_insert_query, record_to_insert)
            self.conn.commit()
            print("success")

    def update_prod_db(self):
        postgres_update_query = """UPDATE "bForAbzal" SET seller = drug_seller, phone_number = their_contacts FROM "attempt_at_22:47" WHERE "bForAbzal".id = "attempt_at_22:47".id """
        self.cur.execute(postgres_update_query)
        self.conn.commit()
        print("success")


Bylygyp = FillDB()
Bylygyp.fill_db_with_product()
# Bylygyp.fill_db_with_seller()
# Bylygyp.update_prod_db()
