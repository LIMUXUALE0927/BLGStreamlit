import streamlit as st

st.set_page_config(
    page_title="BLG赛训工具箱",
    page_icon="🥳",
)

st.write("# 欢迎使用BLG赛训工具箱! 👋")

st.info('BLG赛训工具箱是由小耗子开发、BLG内部使用的赛训相关Python程序集合。')

st.markdown(
    """
    **👈 你可以从左侧边栏选择想要使用的程序!**
    
    ### 每个程序是干什么的?
    - [Leaguepedia](https://limuxuale0927-blgstreamlit-home-hdnf49.streamlitapp.com/Leaguepedia): 英雄联盟全球联赛数据分析程序
    - [DailyRank](https://limuxuale0927-blgstreamlit-home-hdnf49.streamlitapp.com/DailyRank): 批量查询选手每日韩服Rank数量
    - [LeaguePoints](https://limuxuale0927-blgstreamlit-home-hdnf49.streamlitapp.com/LeaguePoints): 批量查询选手韩服排位分数
    - [SearchEngine](https://limuxuale0927-blgstreamlit-home-hdnf49.streamlitapp.com/SearchEngine): 特定比赛对局查询、选手主页导航
    - [PlayerStat](https://limuxuale0927-blgstreamlit-home-hdnf49.streamlitapp.com/PlayerStat): 分析联赛中各位置选手的数据并根据自定权重打分、输出雷达图
    - [Utils](https://limuxuale0927-blgstreamlit-home-hdnf49.streamlitapp.com/Utils): 一些常用工具(如英雄名称翻译)
    
    ### 常用网址 🌐
    - [OP.GG](https://www.op.gg)
    - [Leaguepedia](https://lol.fandom.com/wiki/League_of_Legends_Esports_Wiki)
    - [GOL.GG](https://gol.gg/esports/home/)
    - [Oracle's Elixir](https://oracleselixir.com/stats/players/byTournament)
"""
)
