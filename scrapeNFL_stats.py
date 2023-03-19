import requests
from bs4 import BeautifulSoup
import pandas as pd
from csv import reader
import pprint

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
