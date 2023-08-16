import pandas as pd
import streamlit as st
from riotwatcher import LolWatcher

st.markdown("# 韩服排位分数查询 🎉")

apiKey = st.secrets["my_api"]
lol_watcher = LolWatcher(apiKey)
region = 'kr'


def get_challengers_names():
    my_api = st.secrets["my_api"]
    lol_watcher = LolWatcher(my_api)
    challengers = lol_watcher.league.challenger_by_queue('kr', 'RANKED_SOLO_5x5')
    length = len(challengers['entries'])
    summonerId = [challengers['entries'][i]['summonerId'] for i in range(length)]
    summonerName = [challengers['entries'][i]['summonerName'] for i in range(length)]
    leaguePoints = [challengers['entries'][i]['leaguePoints'] for i in range(length)]
    df_challengers = pd.DataFrame(list(zip(summonerId, summonerName, leaguePoints)),
                                  columns=['summonerId', 'summonerName', 'leaguePoints']).sort_values(by='leaguePoints',
                                                                                                      ascending=False).reset_index(
        drop=True)
    return df_challengers['summonerName'].to_list()


# summoner_list = get_challengers_names()
txt2 = st.text_area("请输入要查询的韩服ID列表，多个ID间请用英文逗号分隔。如果结果出错请刷新页面。",
                    "Dawn u, Kakhi shoot, Let me sup, Radiohead, Agurin모모, hold me3, Chu성훈, NO BUYOUT, DRX Juhana")

namelist2 = txt2.split(',')
namelist2 = [i.strip() for i in namelist2]
namelist2 = [i.replace('\xa0', ' ') for i in namelist2]

stats = pd.DataFrame()
for name in namelist2:
    try:
        summoner_id = lol_watcher.summoner.by_name(region, name)['id']
        data = lol_watcher.league.by_summoner(region, summoner_id)[0]
        record = pd.DataFrame.from_records([data])
        stats = pd.concat([stats, record], ignore_index=True)
    except:
        continue

selected_columns = ['summonerName', 'tier', 'rank', 'leaguePoints', 'wins', 'losses']
stats = stats[selected_columns]
st.dataframe(stats)
