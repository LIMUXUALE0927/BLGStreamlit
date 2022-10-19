import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

st.markdown("# 联赛选手数据分析 🎉")

st.markdown('''
### 使用说明
- 进入[Oracle's Elixir](https://oracleselixir.com/stats/players/byTournament)网站
- 在左侧边栏选择联赛赛区(如LPL)，并选择赛季(如LPL 2022 Summer)
- 点击右上角的 `Download This Table` 下载并保存对应的csv文件
- 点击下方的 `Browse files` 按键上传刚刚下载的csv文件
- 等待 `文件上传成功!` 的字样出现后即可开始使用
''')

st.info("请在下方上传csv文件")
file = st.file_uploader("上传csv文件")

if file is None:
    st.warning("请正确上传文件!")
    st.stop()
if file is not None:
    df = pd.read_csv(file)
    st.success("文件上传成功!")
    st.dataframe(df)

max_GP = int(df['GP'].max())

st.info("请选择筛选条件")
col1, col2 = st.columns(2)
with col1:
    option = st.selectbox("请选择选手位置", ('Top', 'Jungle', 'Middle', 'ADC', 'Support'))
with col2:
    option2 = st.slider("请选择选手最少的出场次数，这将过滤掉出场次数较少的选手", 0, max_GP, 0)

df = df[df['Pos'] == option]
df = df[['Player', 'Team', 'Pos', 'GP', 'KDA', 'KP',
         'KS%', 'DTH%', 'CSPM', 'DPM',
         'DMG%', 'EGPM', 'GOLD%', 'WPM', 'CWPM', 'WCPM']]
df['Vision'] = df['WPM'] + df['CWPM'] + df['WCPM']
df = df.drop(['WPM', 'CWPM', 'WCPM'], axis=1)
df['KP'] = df['KP'].str.strip('%').astype(float) / 100
df['KS%'] = df['KS%'].str.strip('%').astype(float) / 100
df['DTH%'] = df['DTH%'].str.strip('%').astype(float) / 100
df['DMG%'] = df['DMG%'].str.strip('%').astype(float) / 100
df['GOLD%'] = df['GOLD%'].str.strip('%').astype(float) / 100


def min_max(df, column_name):
    df[column_name] = df[column_name].apply(
        lambda x: (x - df[column_name].min()) / (df[column_name].max() - df[column_name].min()))
    return df


df['DTH ADJ'] = 1 - df['DTH%']
df['GOLD CONVERSION'] = df['DPM'] / df['EGPM']
columns = ['KDA', 'KP', 'KS%', 'DTH%', 'CSPM', 'DPM', 'DMG%', 'EGPM', 'GOLD%', 'Vision', 'DTH ADJ', 'GOLD CONVERSION']
for column in columns:
    df = min_max(df, column)

df["生存"] = (df['KDA'] + df['DTH ADJ']) / 2
df["发育/经济"] = (df['CSPM'] + df['EGPM'] + df['GOLD%'] + df['GOLD CONVERSION']) / 4
df["输出/Carry"] = (df['KS%'] + df['DPM'] + df['DMG%']) / 3
df["支援/视野"] = (df['KP'] + df['Vision']) / 2

col1, col2 = st.columns(2)
with col1:
    c1 = st.slider("请选择「生存」在评分中的权重 ", 0.0, 1.0, 0.25)

with col2:
    c2 = st.slider("请选择「发育/经济」在评分中的权重 ", 0.0, 1.0, 0.25)

col3, col4 = st.columns(2)
with col3:
    c3 = st.slider("请选择「输出/Carry」在评分中的权重 ", 0.0, 1.0, 0.25)

with col4:
    c4 = st.slider("请选择「支援/视野」在评分中的权重 ", 0.0, 1.0, 0.25)

df["总分"] = (df["生存"] * c1 + df["发育/经济"] * c2 + df["输出/Carry"] * c3 + df["支援/视野"] * c4) / (c1 + c2 + c3 + c4)

df_scaled = df[['Player', 'Team', 'Pos', 'GP', '生存', '发育/经济', '输出/Carry', '支援/视野', '总分']]
df_scaled = df_scaled.sort_values(by=['总分'], ascending=False)


df_scaled = df_scaled[df_scaled['GP'] >= option2]
df_scaled.reset_index(drop=True, inplace=True)


def highlight_max(s):
    # Get 5 largest values of the column
    is_large = s.nlargest(5).values
    # Apply style is the current value is among the 5 biggest values
    return ['background-color: yellow' if v in is_large else '' for v in s]


df_print = df_scaled
df_print = df_print.style.apply(highlight_max, subset=pd.IndexSlice[:, ['生存', '发育/经济', '输出/Carry', '支援/视野']])
st.dataframe(df_print, width=2000)


st.info("请选择要制作的选手的雷达图")
players = df_scaled.Player.unique().tolist()
player = st.selectbox("请选择选手", players)

df = pd.DataFrame(dict(
    r=df_scaled[df_scaled['Player'] == player].iloc[:, [4, 5, 6, 7]].values.flatten().tolist(),
    theta=['生存', '发育/经济', '输出/Carry', '支援/视野']))
fig = px.line_polar(df, r='r', theta='theta', line_close=True, title=player + "的数据雷达图")
fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1])))
fig.update_traces(fill='toself')

st.plotly_chart(fig, use_container_width=True)
