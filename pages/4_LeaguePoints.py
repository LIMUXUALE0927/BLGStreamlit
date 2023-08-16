import pandas as pd
import streamlit as st
from riotwatcher import LolWatcher

st.markdown("# 韩服排位分数查询 🎉")

apiKey = st.secrets["my_api"]
lol_watcher = LolWatcher(apiKey)
region = 'kr'

txt2 = st.text_area("请输入要查询的韩服ID列表，多个ID间请用英文逗号分隔。如果结果出错请刷新页面。",
                    "Hide on bush, T1 Gumayusi, GEN G Ruler")

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
