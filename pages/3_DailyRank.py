from datetime import datetime
from datetime import timedelta

import streamlit as st
from riotwatcher import LolWatcher

st.markdown("# 日常韩服排位数量查询 🎉")

today = int(datetime.fromisoformat(datetime.today().strftime('%Y-%m-%d 12:00')).timestamp())
yesterday = int(datetime.fromisoformat((datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d 12:00')).timestamp())

txt = st.text_area("请输入要查询的韩服ID列表，多个ID间请用英文逗号分隔。如果结果出错请刷新页面。", "Hide on bush, T1 Gumayusi, GEN G Ruler")
namelist = str(txt).split(',')
namelist = [i.strip() for i in namelist]
namelist = [i.replace('\xa0', ' ') for i in namelist]

my_api = 'RGAPI-72a071f8-44b1-4b69-8cfc-bc34be3c7421'

lol_watcher = LolWatcher(my_api)
region = 'kr'

st.markdown("本次查询时间段: " + (datetime.today() - timedelta(days=1)).strftime(
    '%Y-%m-%d 12:00') + " -- " + datetime.today().strftime('%Y-%m-%d 12:00'))


def count_rank(summoner_name):
    summoner = lol_watcher.summoner.by_name(region, summoner_name)
    puuid = summoner['puuid']
    matchlist = lol_watcher.match.matchlist_by_puuid(region='asia', puuid=puuid, type='ranked',
                                                     start_time=yesterday, end_time=today)
    st.write(summoner_name, ' 打了 ', len(matchlist), ' 场排位。')


for i in namelist:
    try:
        count_rank(i)
    except:
        continue
