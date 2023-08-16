from datetime import datetime
from datetime import timedelta
import pandas as pd
import streamlit as st
from riotwatcher import LolWatcher

st.markdown("# 日常韩服排位数量查询 🎉")

today = int(datetime.fromisoformat(datetime.today().strftime('%Y-%m-%d 12:00')).timestamp())
yesterday = int(datetime.fromisoformat((datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d 12:00')).timestamp())

txt = st.text_area("请输入要查询的韩服ID列表，多个ID间请用英文逗号分隔。如果结果出错请刷新页面。",
                   "Hide on bush, T1 Gumayusi")
namelist = str(txt).split(',')
namelist = [i.strip() for i in namelist]
namelist = [i.replace('\xa0', ' ') for i in namelist]

my_api = st.secrets["my_api"]

lol_watcher = LolWatcher(my_api)
region = 'kr'

st.markdown("本次查询时间段: " + (datetime.today() - timedelta(days=30)).strftime(
    '%Y-%m-%d 12:00') + " -- " + datetime.today().strftime('%Y-%m-%d 12:00'))

rank_df = pd.DataFrame(columns=['韩服ID', '排位数量'])

for i in namelist:
    try:
        summoner = lol_watcher.summoner.by_name(region, i)
        puuid = summoner['puuid']
        matchlist = lol_watcher.match.matchlist_by_puuid(region='asia', puuid=puuid, type='ranked',
                                                         start_time=yesterday, end_time=today)
        data = pd.DataFrame({'韩服ID': [i], '排位数量': [len(matchlist)]})
        rank_df = pd.concat([rank_df, data], ignore_index=True)
    except:
        continue

st.dataframe(rank_df)
