import requests
import pandas as pd
player_name = input("What player?").title()
# season_id = input("What Season? ex) 2020-21: ")

season_list = [
	'1996-97',
	'1997-98',
	'1998-99',
	'1999-00',
	'2000-01',
	'2001-02',
	'2002-03',
	'2003-04',
	'2004-05',
	'2005-06',
	'2006-07',
	'2007-08',
	'2008-09',
	'2009-10',
	'2010-11',
	'2011-12',
	'2012-13',
	'2013-14',
	'2014-15',
	'2015-16',
	'2016-17',
	'2017-18',
	'2018-19',
	'2019-20',
    '2020-21',
    '2021-22'
]

headers  = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'x-nba-stats-origin': 'stats',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

#type_player = 'P'
season_id= '2020-21'
per_mode = 'Totals'
#per_mode = 'PerGame'



player_info_url = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode={}&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season={}&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight='.format(per_mode, season_id)
response = requests.get(url=player_info_url, headers=headers).json()
#print(response)
player_info = response['resultSets'][0]['rowSet']
nba_df = pd.DataFrame(player_info)
player = nba_df[1].str.contains(f'{player_name}')
print(nba_df[player])
data = pd.DataFrame(nba_df[player])
data.to_csv(f"data/NBA_stats_{player_name}.csv", index=False)
#
# productslist = []
# for row in nba_df[player]:
# 	product = {
# 		'season_id' = season_id,
# 		'player_id': row[1],
#     	'player_name': row[2],
#     	'team_id': row[3],
#     	'team_abbreviation': row[4],
#     	'age': row[5],
#     	'gp': row[6],
#     	'w': row[7],
#     	'l': row[8],
#     	'w_pct': row[9],
#     	'min': row[10],
#     	'fgm': row[11],
#     	'fga': row[12],
#     	'fg_pct': row[13],
#     	'fg3m': row[14],
#     	'fg3a': row[15],
#     	'fg3_pct': row[16],
#     	'ftm': row[17],
#     	'fta': row[18],
#     	'ft_pct': row[19],
#     	'oreb': row[20],
#     	'dreb': row[21],
#     	'reb': row[22],
#     	'ast': row[23],
#     	'stl': row[24],
#     	'blk': row[25],
#     	'tov': row[26],
#     	'pf': row[27],
#     	'pts': row[28],
#     	'plus_minus': row[29],
#     	'video_available': row[30],
# 	}

# 	productslist.append(product)
# print(productslist)

# if f'{player_name}' == productslist['player_id']:
# 	print(productslist)
# 	data = pd.DataFrame(productslist)
# 	data.to_csv(f"data/NBA_stats_{player_name}.csv", index=False)


#print(productslist)





