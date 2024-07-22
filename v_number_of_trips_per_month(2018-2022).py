# 사용 라이브러리 호출
import pandas as pd
import numpy as np 

# 전처리 된 데이터 불러오기
p_num_trip = pd.read_excel('pre_data/p_num_trip.xlsx')

# 데이터 정보 확인하기
# p_num_trip(년-월 별 여행 횟수)데이터 정보 확인하기
p_num_trip.info()
p_num_trip.shape
p_num_trip.head()
p_num_trip.describe()

# 분석을 용이하게 하기 위해 년도별 DataFrame생성
y2018 = p_num_trip.query('year == 2018')
y2019 = p_num_trip.query('year == 2019')
y2020 = p_num_trip.query('year == 2020')
y2021 = p_num_trip.query('year == 2021')
y2022 = p_num_trip.query('year == 2022')

# 데이터 시각화
# 시각화 라이브러리 호출
import matplotlib.pyplot as plt

# 그래프에 한글 표시하기
plt.rcParams['font.family'] ='Malgun Gothic'
# 언더바(_) 표시 가능하게 만듬
plt.rcParams['axes.unicode_minus'] =False

# 데이터 시각화

# 1. 2018년 ~ 2022년 기간동안 남녀의 여행 총 횟수를 비교하기
sex_total = [p_num_trip['male'].sum(), p_num_trip['female'].sum()]
sex = ['남성','여성']

# 그래프 제목과 y축 레이블 설정
plt.title("2018 ~ 2022년 5년간 남녀의 총 여행 횟수 추이")
plt.ylabel("단위 : 천회")

# 그래프 표시
# 남성은 하늘색, 여성은 분홍색으로 매칭
plt.bar(sex, sex_total, color=['skyblue','pink'])
plt.show()
plt.clf()

# 2. 2018년도 부터 2020년도 까지 남+여, 남, 여 여행 횟수 증감의 트랜드 구하기
# 데이터 선택

# for x in range 구문을 이용하여 다음과 같은 반복문을 실행
# sex_total2 = [y2018['total'].sum(), 
#               y2019['total'].sum(), 
#               y2020['total'].sum(), 
#               y2021['total'].sum(), 
#               y2022['total'].sum()]

sex_total2 = [x['total'].sum() for x in [y2018, y2019, y2020, y2021, y2022]]
male_total = [x['male'].sum() for x in [y2018, y2019, y2020, y2021, y2022]]
female_total = [x['female'].sum() for x in [y2018, y2019, y2020, y2021, y2022]]
sex_total_mean = [x['total'].mean() for x in [y2018, y2019, y2020, y2021, y2022]]
years = [2018,2019,2020,2021,2022]

# 그래프 제목과 y축 레이블 설정
plt.title("2018 ~ 2022년 남녀의 총 여행 횟수")
plt.ylabel("단위 : 천회")

# 그래프 표시

x_range = np.arange(len(years))
plt.bar(x_range+0.0, sex_total2, width=0.25, label='총합', color = 'green')
plt.bar(x_range+0.3, male_total, width=0.25, label='남성', color = 'blue')
plt.bar(x_range+0.6, female_total, width=0.25, label='여성', color = 'red')
sns.lineplot(x_range+0.3, sex_total_mean, label='총 평균', color = "black")

# x축 라벨 설정
plt.xticks(x_range+0.3, years)

# 범례추가
plt.legend()

# 그래프 보여주기
plt.show()
plt.clf()
              
              











