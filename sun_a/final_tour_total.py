import numpy as np
import pandas as pd
import matplotlib as plt

tour_total = pd.read_csv('pre_data/total_tour.csv',  encoding = 'cp949')
tour_total = pd.read_csv("C:/Users/USER/Documents/LS빅데이터스쿨/team3_project/pre_data/total_tour.csv",encoding = 'cp949')
tour_total.info()

import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# Top 3 순위 구하기
tour_total_rank = tour_total.groupby("spot")\
                            .agg(mean = ("search_count","mean"))
        
tour_total_rank.sort_values(["mean"], ascending=False)

## 각 연도별  TOP 10 관광지 구하기
ranking1 = tour_total.query("spot=='에버랜드'")
ranking2 = tour_total.query("spot=='속초관광수산시장'")
ranking3 = tour_total.query("spot=='코엑스'")

plt.clf()

plt.plot(ranking1["year"], ranking1["search_count"], marker='o', label="에버랜드")
plt.plot(ranking2["year"], ranking2["search_count"], marker='o', label='속초관광수산시장')
plt.plot(ranking3["year"], ranking3["search_count"], marker='o', label='코엑스')

plt.title('상위 3개 관광지 5년 추이')
plt.xlabel('년도')
plt.ylabel('검색수')
plt.legend(title='Spot', bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 5})
plt.grid(True)
plt.tight_layout()
plt.xticks(years)  # x축 눈금 설정
plt.show()
plt.clf()
# 중분류 수정본
# tour_total["year"] = tour_total["year"].astype(int)
# Top 3 순위 구하기
tour_total_c = tour_total.groupby("category_m")\
                            .agg(c_sum = ("search_count","sum"))
        
tour_total_c.sort_values(["c_sum"], ascending=False)

# 연도별
tour_total_c2 = tour_total.groupby(["year","category_m"], as_index=False)\
                            .agg(category_sum = ("search_count","sum"))



ranking4 = tour_total_c2.query("category_m=='쇼핑'")

ranking5 = tour_total_c2.query("category_m=='자연관광'")

ranking6 = tour_total_c2.query("category_m=='문화관광'")


plt.clf()

plt.plot(ranking4["year"], ranking4["category_sum"], marker='o', label="쇼핑")
plt.plot(ranking5["year"], ranking5["category_sum"], marker='o', label='자연관광')
plt.plot(ranking6["year"], ranking6["category_sum"], marker='o', label='문화관광')

plt.title('2018~2022 관광지 중분류 Top3')
plt.xlabel('년도')
plt.ylabel('검색수 (단위: 천만 회)')
plt.legend(title='Spot', bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 5})
plt.grid(True)
plt.tight_layout()
#plt.xticks(years)  # x축 눈금 설정
plt.show()

# 중분류 추이
# 'year'과 'category_m' 열로 그룹화하여 'search_count' 합계 구하기 및 정렬
top10_categories_total = tour_total.groupby(['year', 'category_m']) \
                                   .agg(count_tour=('search_count', 'sum')) \
                                   .reset_index() \
                                   .sort_values(['year', 'count_tour'], ascending=[True, False])

# 각 연도별로 top10 카테고리 추출
years = range(2018, 2023)
top10_categories_total_list = []

for year in years:
    top10_categories_year = top10_categories_total[top10_categories_total['year'] == year].head(3)
    top10_categories_total_list.append(top10_categories_year)

# 시각화를 위해 데이터 재구성
top_categories = pd.concat(top10_categories_total_list)['category_m'].unique()
plot_data = pd.DataFrame(index=years, columns=top_categories)

for year in years:
    yearly_data = top10_categories_total[top10_categories_total['year'] == year].set_index('category_m')
    for category in top_categories:
        if category in yearly_data.index:
            plot_data.at[year, category] = yearly_data.at[category, 'count_tour']
        else:
            plot_data.at[year, category] = 0

# 그래프 그리기
plt.figure(figsize=(4, 2))
for category in top_categories:
    plt.plot(plot_data.index, plot_data[category], marker='o', label=category)

plt.title('<2018~2022 관광지 중분류 Top 3>')
plt.xlabel('년도')
plt.ylabel('검색수 (단위: 천만 회)')
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 7})
plt.grid(True)
plt.tight_layout()
plt.show()
plt.clf()

