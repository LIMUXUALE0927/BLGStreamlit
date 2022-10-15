import pandas as pd
import streamlit as st
from riotwatcher import LolWatcher

st.markdown("# 韩服排位分数查询 🎉")

apiKey = st.secrets["my_api"]
lol_watcher = LolWatcher(apiKey)
region = 'kr'

txt = st.text_area("请输入要查询的韩服ID列表，多个ID间请用英文逗号分隔。如果结果出错请刷新页面。", "Hide on bush, T1 Gumayusi, GEN G Ruler")

namelist = txt.split(',')
namelist = [i.strip() for i in namelist]
namelist = [i.replace('\xa0', ' ') for i in namelist]

stats = pd.DataFrame()
for name in namelist:
    try:
        summoner_id = lol_watcher.summoner.by_name(region, name)['id']
        data = lol_watcher.league.by_summoner(region, summoner_id)
        stats = stats.append(data, ignore_index=True)
    except:
        continue

st.table(stats[['summonerName', 'tier', 'rank', 'leaguePoints']])


@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')


data = stats[['summonerName', 'tier', 'rank', 'leaguePoints']]
csv = convert_df(data)

st.download_button(
    label="下载数据",
    data = csv,
    file_name='韩服分数.csv'
)