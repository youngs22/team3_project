import numpy as np
import pandas as pd

#데이터 파악하기
tour_2018 = pd.read_csv('data/ranking_2018.csv', encoding = 'cp949')
tour_2019 = pd.read_csv('data/ranking_2019.csv', encoding = 'cp949')
tour_2020 = pd.read_csv('data/ranking_2020.csv', encoding = 'cp949')
tour_2021 = pd.read_csv('data/ranking_2021.csv', encoding = 'cp949')
tour_2022 = pd.read_csv('data/ranking_2022.csv', encoding = 'cp949')
#전처리
# 열 이름 출력
column_names = tour_2018.columns.tolist()
print(column_names)

tour_2018 = tour_2018.rename(columns = {'순위'      : 'ranking',    \
                                        '광역시/도' : 'state',       \
                                        '시/군/구'  : 'city',   \
                                        '관광지명'  : 'spot', \
                                        '도로명주소': 'address',    \
                                        '중분류 카테고리': 'category_m', \
                                        '소분류 카테고리': 'category_s', \
                                        '검색건수':        'search_count'
                                          })
tour_2019 = tour_2019.rename(columns = {'순위'      : 'ranking',    \
                                        '광역시/도' : 'state',       \
                                        '시/군/구'  : 'city',   \
                                        '관광지명'  : 'spot', \
                                        '도로명주소': 'address',    \
                                        '중분류 카테고리': 'category_m', \
                                        '소분류 카테고리': 'category_s', \
                                        '검색건수':        'search_count'
                                          })
tour_2020 = tour_2020.rename(columns = {'순위'      : 'ranking',    \
                                        '광역시/도' : 'state',       \
                                        '시/군/구'  : 'city',   \
                                        '관광지명'  : 'spot', \
                                        '도로명주소': 'address',    \
                                        '중분류 카테고리': 'category_m', \
                                        '소분류 카테고리': 'category_s', \
                                        '검색건수':        'search_count'
                                          })
tour_2021 = tour_2021.rename(columns = {'순위'      : 'ranking',    \
                                        '광역시/도' : 'state',       \
                                        '시/군/구'  : 'city',   \
                                        '관광지명'  : 'spot', \
                                        '도로명주소': 'address',    \
                                        '중분류 카테고리': 'category_m', \
                                        '소분류 카테고리': 'category_s', \
                                        '검색건수':        'search_count'
                                          })
tour_2022 = tour_2022.rename(columns = {'순위'      : 'ranking',    \
                                        '광역시/도' : 'state',       \
                                        '시/군/구'  : 'city',   \
                                        '관광지명'  : 'spot', \
                                        '도로명주소': 'address',    \
                                        '중분류 카테고리': 'category_m', \
                                        '소분류 카테고리': 'category_s', \
                                        '검색건수':        'search_count'
                                          })
cate_remove = ['교통시설', '면세점', '백화점','쇼핑몰', '대형마트', '기타쇼핑시설']
tour_2018 = tour_2018[~tour_2018['category_s'].isin(cate_remove)]
print(tour_2018['category_s'].unique())

cate_remove = ['교통시설', '면세점', '백화점', '쇼핑몰', '대형마트', '기타쇼핑시설']
tour_2019 = tour_2019[~tour_2019['category_s'].isin(cate_remove)]
print(tour_2019['category_s'].unique())

cate_remove = ['교통시설', '면세점', '백화점', '쇼핑몰', '대형마트', '기타쇼핑시설']
tour_2020 = tour_2020[~tour_2020['category_s'].isin(cate_remove)]
print(tour_2020['category_s'].unique())

cate_remove = ['교통시설', '면세점', '백화점', '쇼핑몰', '대형마트', '기타쇼핑시설']
tour_2021 = tour_2021[~tour_2021['category_s'].isin(cate_remove)]
print(tour_2021['category_s'].unique())

cate_remove = ['교통시설', '면세점', '백화점', '쇼핑몰', '대형마트', '기타쇼핑시설']
tour_2022 = tour_2022[~tour_2022['category_s'].isin(cate_remove)]
print(tour_2022['category_s'].unique())

#top 30 추출하기
tour_2018 = tour_2018.sort_values(by = 'search_count', ascending = False).head(30)
tour_2018
tour_2019 = tour_2019.sort_values(by = 'search_count', ascending = False).head(30)
tour_2019
tour_2020 = tour_2020.sort_values(by = 'search_count', ascending = False).head(30)
tour_2020
tour_2021 = tour_2021.sort_values(by = 'search_count', ascending = False).head(30)
tour_2021
tour_2022 = tour_2022.sort_values(by = 'search_count', ascending = False).head(30)
tour_2022

tours = [tour_2018, tour_2019, tour_2020, tour_2021, tour_2022]

# concat 함수를 사용하여 데이터프레임들을 행 방향으로 합칩니다.
tour_top30 = pd.concat(tours, ignore_index=True)

# 합친 결과 확인
print(tour_top30)

tour_top30 = tour_top30.drop(columns=['address'])
tour_top30.info()
tour_top30.shape
tour_top30.to_excel('pre_tour_top30.xlsx', index=False)

# commit test용 
# 전처리한 데이터 파일 추출
# route.to_excel('pre_route.xlsx', index=False)
