# 라이브러리 호출
! pip install numpy
! pip install pandas

import pandas as pd
import numpy as np

! pip install openpyxl

# 데이터 불러오기
# header를 두번째 행으로 고정
num_trip = pd.read_excel('pre_data/R_월별_국내여행_횟수_20240714204514.xlsx', header=1)
num_trip.nunique()

# 데이터 전처리

# 열(columns)의 변수명 변경

# 시점
num_trip = num_trip.rename(columns = { '시점' : 'year', '항목' : 'month'})

# 전체
num_trip = num_trip.rename(columns = { '소계' : 'total'})

# 성별
num_trip = num_trip.rename(columns = { '남자' : 'male', '여자' :'female'})


# 학력
num_trip = num_trip.rename(columns = { '초졸 이하' : 'elmt', '중학교' : 'mid',
						               '고등학교' : 'high', '대학교이상' : 'univ+'})

# 가구원수
num_trip = num_trip.rename(columns = { '1인' : 'per1',
						               '2인' : 'per2',
						               '3인이상' : 'per3+'})

# 열(columns)의 파생변수 생성
# 연령 
# 15~19세, 20대, 30대, 40대, 50대, 60대, 70세 이상을 청소년, 청년, 중년, 노년 층으로 구분
num_trip["teens"] = num_trip["15~19세"]
num_trip["young_adults"] = num_trip["20대"] + num_trip["30대"]
num_trip["middle_adults"] = num_trip["40대"] + num_trip["50대"]
num_trip["seniors"] = num_trip["60대"] + num_trip["70세 이상"]

# 15~19세, 20대, 30대, 40대, 50대, 60대, 70세 이상 열 삭제
num_trip = num_trip.drop(num_trip.columns[np.arange(5,12,1)], axis=1)

# 


num_trip.info()





# 직업 - 직업과 여행 횟수간의 상관관계가 크게 없다고 판단하여
# 임금봉급근로자, 고용원있는사업주, 고용원없는자영업자
# 무급가족 종사자, 사무전문, 기술생산노무, 판매서비스
# 자영업, 학생, 전업주부, 무직은퇴, 기타
# 12개의 열 삭제
num_trip = num_trip.drop(num_trip.columns[np.arange(12,24,1)], axis=1)




num_trip

# 데이터 전처리
# 첫 행 제거
num_trip.drop([0])
num_trip.drop[0]
