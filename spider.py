import requests
import pandas as pd
from io import StringIO


url = "https://lotto.sina.cn/trend/qxc_qlc_proxy.d.html?lottoType=ssq&actionType=chzs&0_ala_h5baidu&_headline=baidu_ala&type=500"


headers = {
    "User-Agent":
    "Mozilla/5.0"
}


response = requests.get(
    url,
    headers=headers
)

response.encoding = "utf-8"


html = response.text


# 读取表格

tables = pd.read_html(
    StringIO(html)
)


df = tables[0]


print("原始数据:")
print(df.shape)



# ==========================
# 处理多级表头
# ==========================

df.columns = [
    "_".join(col).strip()
    for col in df.columns
]


print("\n处理后的列名:")
print(df.columns)



# ==========================
# 保存原始走势图
# ==========================

df.to_csv(
    "ssq_raw.csv",
    encoding="utf-8-sig",
    index=False
)


print("\n原始走势图保存完成")