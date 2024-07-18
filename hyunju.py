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

#볼거리 제공 
visualappeal = total_all.query("item == '볼거리 제공'")
visualappeal.polt.bar(rot = 0)
plt.show()


















