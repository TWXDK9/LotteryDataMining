import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://lotto.sina.cn/trend/qxc_qlc_proxy.d.html?lottoType=ssq&actionType=chzs&0_ala_h5baidu&_headline=baidu_ala&type=500"


headers = {
    "User-Agent":
    "Mozilla/5.0"
}


# 获取网页

response = requests.get(
    url,
    headers=headers,
    timeout=10
)

response.encoding = "utf-8"

html = response.text



# 解析HTML

soup = BeautifulSoup(
    html,
    "html.parser"
)



table = soup.find(
    "table",
    id="chartsTable"
)



rows = table.find(
    "tbody"
).find_all(
    "tr"
)



data = []



for row in rows:


    cells = row.find_all("td")


    # 期号

    issue = cells[0].get_text(strip=True)



    red = []

    blue = None



    for cell in cells:


        cls = cell.get("class")


        if not cls:
            continue


        text = cell.get_text(strip=True)



        if not text.isdigit():
            continue



        # 红球

        if "chartball01" in cls:

            red.append(
                f"{int(text):02d}"
            )


        # 蓝球

        if "chartball02" in cls:

            blue = f"{int(text):02d}"



    # 正常开奖才保存

    if len(red) == 6 and blue is not None:


        data.append({

            "期号": issue,

            "红1": red[0],
            "红2": red[1],
            "红3": red[2],
            "红4": red[3],
            "红5": red[4],
            "红6": red[5],

            "蓝球": blue

        })



# 转DataFrame

df = pd.DataFrame(data)



print("===================")
print(df.head())


print("===================")
print("数据量:")
print(df.shape)



# 保存

df.to_csv(
    "ssq_result.csv",
    encoding="utf-8-sig",
    index=False
)



print("保存完成: ssq_result.csv")