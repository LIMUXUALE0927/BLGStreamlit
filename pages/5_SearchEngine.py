import streamlit as st

st.markdown("# 英雄联盟数据搜索引擎 🎉")

st.markdown("### 2支队伍的历史对阵信息")
st.info("例: 想查询RNG和EDG的历史交手比赛信息，在下方2个输入框输入 RNG 和 EDG ，再点击生成查询链接即可，输入顺序不影响结果。")

col1, col2 = st.columns(2)
with col1:
    team1 = st.text_input("请输入队伍1名称")
with col2:
    team2 = st.text_input("请输入队伍2名称")

s = f"https://lol.fandom.com/Special:RunQuery/MatchHistoryGame?MHG%5Bspl%5D=yes&MHG%5Bteam1%5D={team1}&MHG%5Bteam2%5D={team2}&MHG%5Bpreload%5D=TeamHeadToHead&_run="

if st.button("生成查询链接"):
    st.success(s)


st.markdown("---")

st.markdown("### 选手资料页导航")
st.info("例: 想进入Uzi的选手资料页，在下方输入框输入 Uzi ，再点击生成查询链接即可。")

player_name = st.text_input("请输入选手比赛ID")
s1 = f"https://lol.fandom.com/wiki/Special:Search?query={player_name}&scope=internal&navigationSearch=true"
s2 = f"https://www.carrystats.com/lol/search?k={player_name}"

if st.button("生成查询链接", key=2):
    st.success("Leaguepedia: " + s1)
    st.success("玩加电竞: " + s2)