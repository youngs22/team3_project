import numpy as np
import pandas as pd

tour_total = pd.read_csv('pre_data/total_tour.csv',  encoding = 'cp949')
tour_total.info()

import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# 1. 중분류 빈도 확인하기
count_city = tour_total['category_m'].value_counts().head(10)
plt.figure(figsize=(3, 1))
count_city.plot.bar(rot=0)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)
# 여백을 수동으로 조정합니다.
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
# 글자가 잘리지 않도록 레이아웃을 자동으로 조정합니다.
plt.tight_layout()
# 그림을 표시합니다.
plt.title('<2018년~2022년 중분류 빈도수>')
plt.xlabel('관광지 중분류')
plt.ylabel('빈도수 (단위: 회)')
plt.show()
# 이후 그래프를 초기화합니다.
plt.clf()

# 2. 각 연도별 TOP 5 지역 구하기
# 'year'과 'combined_city' 열로 그룹화하여 'search_count' 합계 구하기
# top10_cities_per_year -> top10_cities
top10_cities = tour_total.groupby(['year', 'combined_city']) \
                                 .agg(count_tour=('search_count', 'sum')) \
                                 .reset_index() \
                                 .sort_values(['year', 'count_tour'], ascending=[True, False])

# 3. 5년 top5 도시 시각화
import pandas as pd
import matplotlib.pyplot as plt

# 예시 데이터 로드
# tour_total = pd.read_csv('tour_total.csv')

# 그룹화 및 정렬
top10_cities_total = tour_total.groupby(['year', 'combined_city']) \
                               .agg(count_tour=('search_count', 'sum')) \
                               .reset_index() \
                               .sort_values(['year', 'count_tour'], ascending=[True, False])

# 연도별 top5 도시 추출
years = range(2018, 2023)
top10_cities_total_list = []

for year in years:
    top10_cities_year = top10_cities_total[top10_cities_total['year'] == year].head(2)
    top10_cities_total_list.append(top10_cities_year)

# 시각화를 위해 데이터 재구성
top_cities = pd.concat(top10_cities_total_list)['combined_city'].unique()
plot_data = pd.DataFrame(index=years, columns=top_cities)

for year in years:
    yearly_data = top10_cities_total[top10_cities_total['year'] == year].set_index('combined_city')
    for city in top_cities:
        if city in yearly_data.index:
            plot_data.at[year, city] = yearly_data.at[city, 'count_tour']
        else:
            plot_data.at[year, city] = 0

# 그래프 그리기
plt.figure(figsize=(4, 2))
for city in top_cities:
    plt.plot(plot_data.index, plot_data[city], marker='o', label=city)

plt.title('<2018~2022 관광 지역 Top 5>')
plt.xlabel('년도')
plt.ylabel('총 검색 수 (단위: 백만 회)')
plt.legend(title='City', bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 6})
plt.grid(True)
plt.xticks(years)  # x축 눈금 설정
plt.tight_layout()
plt.show()
plt.clf()
# 단위: 백만 회(ex: 1.5 -> 150만)

#중분류 추이
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

# 소분류 추이
import pandas as pd
import matplotlib.pyplot as plt

# 예시 데이터프레임 (실제 데이터로 대체해야 함)
# tour_total = pd.read_csv('tour_data.csv')

# 'year'과 'category_s' 열로 그룹화하여 'search_count' 합계 구하기 및 정렬
top10_categories_s_total = tour_total.groupby(['year', 'category_s']) \
                                     .agg(count_tour=('search_count', 'sum')) \
                                     .reset_index() \
                                     .sort_values(['year', 'count_tour'], ascending=[True, False])

# 각 연도별로 top10 소분류 추출
years = range(2018, 2023)
top10_categories_s_total_list = []

for year in years:
    top10_categories_s_year = top10_categories_s_total[top10_categories_s_total['year'] == year].head(3)
    top10_categories_s_total_list.append(top10_categories_s_year)

# 시각화를 위해 데이터 재구성
top_categories_s = pd.concat(top10_categories_s_total_list)['category_s'].unique()
plot_data = pd.DataFrame(index=years, columns=top_categories_s)

for year in years:
    yearly_data = top10_categories_s_total[top10_categories_s_total['year'] == year].set_index('category_s')
    for category in top_categories_s:
        if category in yearly_data.index:
            plot_data.at[year, category] = yearly_data.at[category, 'count_tour']
        else:
            plot_data.at[year, category] = 0

# 그래프 그리기
plt.figure(figsize=(4, 2))
for category in top_categories_s:
    plt.plot(plot_data.index, plot_data[category], marker='o', label=category)

plt.title('<2018~2022 관광지 소분류 Top 3>')
plt.xlabel('년도')
plt.ylabel('총 검색 수 (단위: 백만 회)')
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 6})
plt.grid(True)
plt.xticks(years)  # x축 눈금 설정
plt.tight_layout()
plt.show()

plt.clf()
# 단위: 백만
