import requests
from bs4 import BeautifulSoup

 



class Item:
    name = None
    value = None
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __str__(self):
        return(f"{self.name}:{self.value}")
user_agent = {'User-agent': 'Mozilla/5.0'}
url = "https://www.fresh-market.info/price-quotations/poland/bronisze-warsaw"
page = requests.get(url, headers=user_agent)

soup = BeautifulSoup(page.content, "html.parser")

table = soup.find(id="pelna_tabela_1995099854")
rows = table.find_all("tr")
def get_current_prices(scrapped_products, scrapped_unit):
    scrapped_items = []
    for row in rows:
        itemName = None
        correctUnit = False
        price_sum = 0
        entities = row.find_all("td")
        for entity in entities:
            for product in scrapped_products:
                if str(product) == entity.get_text():
                    itemName = entity.get_text()
            if scrapped_unit in entity.get_text():
                correctUnit = True
            if str("€") in entity.get_text():
                price_sum += float(entity.get_text()[:-2])
        if itemName is not None and correctUnit is True:
            price = round(price_sum/2, 4)
            newItem = Item(name=itemName, value=price)
            scrapped_items.append(newItem)
    return scrapped_items

        
