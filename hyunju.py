import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 한글 설정
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

df = pd.read_excel("./pre_data/pre_select.xlsx")
df

df_2018 = df.loc[0:14]
df_2019 = df.loc[15:29]
df_2020 = df.loc[30:44]
df_2021 = df.loc[45:59]
df_2022 = df.loc[60:74]
df_2018.dtypes()

total_2018 = df_2018.sort_values("total", ascending = False).head()
total_2019 = df_2019.sort_values("total", ascending = False).head()
total_2020 = df_2020.sort_values("total", ascending = False).head()
total_2021 = df_2021.sort_values("total", ascending = False).head()
total_2022 = df_2022.sort_values("total", ascending = False).head()

total_all = pd.concat([total_2018, total_2019, total_2020, total_2021, total_2022]).iloc[:, :3]
total_all_pivot = total_all.pivot(index='year', columns='item', values='total')
total_all_pivot.plot(kind='bar', figsize=(10, 6))

plt.title('년도별 여행지 선택 5순위')
plt.xlabel('Year')
plt.ylabel('Total')
plt.legend(title='Item', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=0)  # x축 레이블을 수평으로 설정
plt.show()
plt.clf()
---------------------------------------------------------------------------------

#볼거리 제공 선 그래프
visualappeal = total_all.query("item == '볼거리 제공'")
Popularity = total_all.query("item == '여행지 지명도'")
time = total_all.query("item == '여행할 수 있는 시간'")


# 선 그래프 생성
plt.figure(figsize=(10, 6))
plt.plot(visualappeal["year"], visualappeal["total"], marker='o',label="볼거리 제공")
plt.plot(Popularity["year"], Popularity["total"], marker='o',label="여행지 지명도")
plt.plot(time["year"], time["total"], marker='o',label="여행할 수 있는 시간")


# 그래프에 제목과 축 레이블 추가
plt.title("여행을 선택하는 이유 - 전체")
plt.xlabel("년도")
plt.ylabel("전체 %")
plt.legend(fontsize='x-small',loc='center left')
plt.show()
---------------------------------------------------------------------------------
# 남녀의 여행 선택 차이
male_all = df[["male", "item"]]
female_all = df[["female", "item"]]

male_2018 = df_2018[["item","male"]].sort_index("item")















