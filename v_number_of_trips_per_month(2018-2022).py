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

# 데이터 시각화
# 시각화 라이브러리 호출
import matplotlib.pyplot as plt

# 그래프에 한글 표시하기
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# 1. 2018년 ~ 2022년 기간동안 남녀의 여행 총 횟수를 비교하기
sex_total = [p_num_trip['male'].sum(), p_num_trip['female'].sum()]
sex = ['남성','여성']
plt.bar(sex, sex_total)
plt.title("2018 ~ 2022년 남녀의 총 여행 횟수")
plt.ylabel("단위 : 천회")
plt.show()
plt.clf()
