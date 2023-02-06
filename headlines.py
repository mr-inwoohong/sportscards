import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

search = input('Who are you looking for?')
search = search.replace(' ', '')

url = f'https://news.google.com/rss/search?q={search}'

r = requests.get(url)
soup = BeautifulSoup(r.text, features="xml")
#print(soup)

results = soup.find_all('item')
link = soup.find('link')
print(results)

productslist = []
for item in results:
    product = {
        'title': item.find('title').text,
        'link': item.find('link').text,
    }
    productslist.append(product)
print(productslist)

data = pd.DataFrame(productslist)
data.to_csv(f"data/headlines{search}.csv", index=False)


#soup.select('.heading') - name of class
#for 'id'# name = soup.select_one(selector='name') - name of id is name
#company_url = soup.select_one(selector='p a')
#heading = soup.find(name='h1', id/class='name')
# all_anchor_tags = soup.find_all(name='a')
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get('href'))
