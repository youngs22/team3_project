import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


route = pd.read_excel("C:/Users/USER/Documents/LS빅데이터스쿨/team3_project/pre_data/pre_route.xlsx")
route.head(10)


# 경로 평균 백분율 막대그래프
## 1. 5개년 평균 경로 순위 구하기
route2=route.groupby("access_path")\
.agg(total_mean = ("total","mean"))
route2

route2 = route2.sort_values(["total_mean"], ascending = False)
route2

## 2. 그래프화 화기
plt.clf()
plt.rcParams['font.family'] ='Malgun Gothic'
plt.subplots_adjust(bottom=0.2)
sns.barplot(data=route2, x="access_path", y="total_mean", palette = "Set1")
plt.xlabel('여행 정보 획득 경로')
plt.ylabel('소계')
plt.xticks(rotation=20)
plt.xticks(fontsize=8)
plt.title('5개년 평균 여행 정보 획득 경로',fontsize=15)
plt.show()




# 연도별로 정보 획득 경로 순위 어떻게 변하는지
route_path = route.groupby(['year', 'access_path'])['total'].mean().unstack()
plt.clf()

plt.figure(figsize=(12, 6))
route_path.plot()

plt.subplots_adjust(right=0.71)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.rcParams['font.family'] ='Malgun Gothic'
plt.title('연도 별 여행 정보 획득 경로',fontsize=15)
plt.show()



# 경로 Top 4에서는 어떤 가구수가 많이 이용하는지 -> 연도합평균
route_p = route[route['access_path'].isin(['acquaintance', 'experience', 'no_information', 'internet_mobile_app'])]
route_per = route_p.groupby('access_path')[["per1","per2","per3+"]].mean()
route_per

path = route_p['access_path'].unique()
index = np.arange(len(path))
bar_width=0.2

plt.clf()
plt.bar(index, route_per["per1"], bar_width, label="per1")
plt.bar(index + bar_width, route_per["per2"], bar_width, label="per2")
plt.bar(index + 2 * bar_width, route_per["per3+"], bar_width, label="per3+")

plt.rcParams['font.family'] ='Malgun Gothic'
plt.xlabel('여행 정보 획득 경로 Top 4')
plt.title('여행 정보 획득 경로 Top 4 : 가구원 수',fontsize=15)
plt.xticks(index + bar_width, path, fontsize=8)
plt.legend()
plt.show()




route_per=route.groupby("access_path")\.agg(total_mean = ("total","mean"))
route_per




# 경로 Top 4에서는 어떤 성별이 많이 이용하는지 -> 연도합평균





# 경로 Top 4에서는 어떤 연령대가 많이 이용하는지 -> 연도합평균







# 경로 Top 3에서는 어떤 소득층이 많이 이용하는지 -> 연도합평균
## 1등-지인추천
route_exp = route[route['access_path'] == 'acquaintance']
route_exp = route_exp.groupby('year')[['l_sal', 'm_sal', 'h_sal']].mean()

years = route_exp['year'].unique()
index = np.arange(len(years))
bar_width=0.2

## 막대 그래프 그리기
plt.clf()

plt.bar(index, route_exp['l_sal'], bar_width, label='l_sal')
plt.bar(index + bar_width, route_exp['m_sal'], bar_width, label='m_sal')
plt.bar(index + 2 * bar_width, route_exp['h_sal'], bar_width, label='h_sal')

plt.xlabel('Year')
plt.ylabel('Salary')
plt.title('Yearly Travel Information Acquisition Rate by Income:Acquaintance',fontsize=10)
plt.xticks(index + bar_width, years)
plt.legend()
plt.show()


## 2등-경험
route_exp = route[route['access_path'] == 'experience']
route_exp = route_exp.groupby('year')[['l_sal', 'm_sal', 'h_sal']].mean()

years = route_exp['year'].unique()
index = np.arange(len(years))
bar_width=0.2

## 막대 그래프 그리기
plt.clf()

plt.bar(index, route_exp['l_sal'], bar_width, label='l_sal')
plt.bar(index + bar_width, route_exp['m_sal'], bar_width, label='m_sal')
plt.bar(index + 2 * bar_width, route_exp['h_sal'], bar_width, label='h_sal')

plt.xlabel('Year')
plt.ylabel('Salary')
plt.title('Yearly Travel Information Acquisition Rate by Income:Experience',fontsize=10)
plt.xticks(index + bar_width, years)
plt.legend()
plt.show()


## 3등-정보없이
route_exp = route[route['access_path'] == 'no_information']
route_exp = route_exp.groupby('year')[['l_sal', 'm_sal', 'h_sal']].mean()

years = route_exp['year'].unique()
index = np.arange(len(years))
bar_width=0.2

## 막대 그래프 그리기
plt.clf()

plt.bar(index, route_exp['l_sal'], bar_width, label='l_sal')
plt.bar(index + bar_width, route_exp['m_sal'], bar_width, label='m_sal')
plt.bar(index + 2 * bar_width, route_exp['h_sal'], bar_width, label='h_sal')

plt.xlabel('Year')
plt.ylabel('Salary')
plt.title('Yearly Travel Information Acquisition Rate by Income:No_information',fontsize=10)
plt.xticks(index + bar_width, years)
plt.legend()
plt.show()


# 경로 순위
route.sort_values(["total"],ascending=False).head(5)
route.head(10)
