import streamlit as st

st.markdown("# 英雄联盟数据搜索引擎 🎉")

st.markdown("### 2支队伍的历史对阵信息")
st.info("例: 想查询RNG和EDG的历史交手比赛信息，在下方2个输入框输入 RNG 和 EDG ，再点击生成查询链接即可，输入顺序不影响结果。")
team1 = st.text_input("请输入队伍1名称")
team2 = st.text_input("请输入队伍2名称")

s = f"https://lol.fandom.com/Special:RunQuery/MatchHistoryGame?MHG%5Bspl%5D=yes&MHG%5Bteam1%5D={team1}&MHG%5Bteam2%5D={team2}&MHG%5Bpreload%5D=TeamHeadToHead&_run="

if st.button("生成查询链接"):
    st.success(s)

