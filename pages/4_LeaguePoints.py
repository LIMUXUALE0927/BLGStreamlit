import pandas as pd
import streamlit as st
from riotwatcher import LolWatcher

st.markdown("# 韩服排位分数查询 🎉")

apiKey = st.secrets["my_api"]
lol_watcher = LolWatcher(apiKey)
region = 'kr'

txt2 = st.text_area("请输入要查询的韩服ID列表，多个ID间请用英文逗号分隔。如果结果出错请刷新页面。", "Hide on bush, T1 Gumayusi, GEN G Ruler")

namelist2 = txt2.split(',')
namelist2 = [i.strip() for i in namelist2]
namelist2 = [i.replace('\xa0', ' ') for i in namelist2]

stats = pd.DataFrame()
for name in namelist2:
    try:
        summoner_id = lol_watcher.summoner.by_name(region, name)['id']
        data = lol_watcher.league.by_summoner(region, summoner_id)
        stats = stats.append(data, ignore_index=True)
    except:
        continue

stats = stats[stats['queueType']=='RANKED_SOLO_5x5']
st.table(stats[['summonerName', 'tier', 'leaguePoints']])

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')


data = stats[['summonerName', 'tier', 'leaguePoints']]
csv = convert_df(data)

st.download_button(
    label="下载数据",
    data = csv,
    file_name='韩服分数.csv',
    mime = 'text/csv',
)