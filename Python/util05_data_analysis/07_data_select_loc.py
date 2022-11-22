import pandas as pd
df = pd.read_excel('slam_score.xlsx', index_col='지원번호')

# print(df.loc['1번']) # index 1번 데이터

# print(df.loc['1번','국어']) # index 1번 데이터 중 국어 데이터

# print(df.loc[['1번','2번'],['영어','수학']]) # index 1번,2번 데이터 중 영어,수학 데이터

# print(df.loc['1번':'5번', '국어':'과학']) # index 1번~5번, 데이터 국어~과학

# print(df.iloc[4]) # 4번 데이터

# print(df.iloc[0:5]) # 0~4 번 데이터

# print(df.iloc[0,0]) # 0,0 데이터

print(df.iloc[[0,1],[0,2]]) # 0,1번의 0,2번항목 데이터