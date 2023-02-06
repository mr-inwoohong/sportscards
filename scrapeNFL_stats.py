import requests
from bs4 import BeautifulSoup
import pandas as pd
from csv import reader
import pprint
# from yahoo_oauth import OAuth2
# import yahoo_fantasy_api as yfa

# YAHOO ASS
# app_id = '5HVeCqGr'
# client_id = 'dj0yJmk9UzdtT29Wc0VZUUhsJmQ9WVdrOU5VaFdaVU54UjNJbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTRi'
# client_secret = 'c07d403eed881901c69e09069957216951cdd58a'
#
# params = {
#     "access_token": '',
#     "consumer_key": client_id,
#     "consumer_secret": client_secret,
#     "refresh_token": '',
#     "token_time": 1433553339.706037,
#     "token_type": "bearer"
# }
#
# sc = OAuth2(None, None, from_file='oauth2.json')



# pro football - barely worked on!!!


year = input('What year?')
player_name = input('What player?').title().replace('*', '', 1).replace('+', '', 1)
football_url = f'https://www.pro-football-reference.com/years/{year}/fantasy.htm'
savesearch = player_name.replace(' ', '')


r = requests.get(football_url)
soup = BeautifulSoup(r.text, 'html.parser')
productslist = []
headers = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]
headers = headers[1:]
rows = soup.findAll('tr', class_=lambda table_rows: table_rows != "thead")
player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]
player_stats = player_stats[2:]
stats = pd.DataFrame(player_stats, columns=headers)
print(stats)

player = stats['Player'].str.contains(f'{player_name}')
print(stats[player])
data = pd.DataFrame(stats[player])
data.to_csv(f"data/stats{savesearch}.csv", index=False)