import pandas as pd
import streamlit as st
import lol_id_tools as lit
import requests

st.markdown("# 常用工具 🎉")

st.markdown("### 英雄名称英翻中")

# ---------------------------------------
latest_version = requests.get(
    "https://ddragon.leagueoflegends.com/api/versions.json"
).json()[0]


def get_ddragon_url(latest_version, locale: str, object_type: str):
    dd_url = "https://ddragon.leagueoflegends.com"

    return f"{dd_url}/cdn/{latest_version}/data/{locale}/{object_type}.json"

@st.cache
def parse_champions(full_patch: str, locale: str = "en_US"):
    url = get_ddragon_url(full_patch, locale, "champion")
    data = requests.get(url).json()

    return {
        int(champion_dict["key"]): champion_dict["name"]
        for champion_dict in data["data"].values()
    }


map = parse_champions(latest_version)
champions = list(map.values())
champ_dict = {champ: lit.get_translation(champ, 'zh_CN', object_type='champion') for champ in champions}
# -------------------------------------------------

sample = '''Aatrox
Braum
Caitlyn
Diana
Evelynn'''
txt = st.text_area("输入英雄英文名称，每个英雄名称占一行", sample)
df = pd.DataFrame(txt.split())
df.columns = ["en"]
df["zh"] = df["en"].map(champ_dict)
st.dataframe(df)


st.markdown("### 英雄名称中英对照表")
st.dataframe({
    "en": champ_dict.keys(),
    "zh": champ_dict.values()
})