import streamlit as st

st.set_page_config(
    page_title="BLG赛训工具箱",
    page_icon="🥳",
)

st.write("# 欢迎使用BLG赛训工具箱! 👋")

st.info('BLG赛训工具箱是由BLG内部开发的赛训相关python程序集合。')

st.markdown(
    """
    **👈 你可以从左侧边栏选择想要使用的程序!**
    
    ### 每个程序是干什么的?
    - Leaguepedia: 英雄联盟全球联赛数据分析程序
    - DailyRank: 批量查询选手每日韩服Rank数量
    - LeaguePoints: 批量查询选手韩服排位分数
    - SearchEngine: 特定比赛对局查询
    - Utils: 一些常用工具(如英雄名称翻译)
    
    ### 常用网址
    - [OP.GG](https://www.op.gg)
    - [Leaguepedia](https://lol.fandom.com/wiki/League_of_Legends_Esports_Wiki)
    - [GOL.GG](https://gol.gg/esports/home/)
    - [Oracle's Elixir](https://oracleselixir.com/stats/players/byTournament)
"""
)