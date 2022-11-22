import pandas as pd
df = pd.read_excel('slam_score.xlsx')

# print(df.describe()) # 자료의 최소, 최대, 평균, 표준편차등을 표시

# print(df.info()) # 자료의 타입, 공백인지 표시

# print(df.head()) # 처음 5개 자료

# print(df.head(7)) # 개수 지정 가능

# print(df.tail()) # 마지막 5개 자료, 마찬가지 개수 지정 가능

# print(df.values) # 자료값

# print(df.index) # 인덱스

# print(df.columns) # 데이터 행

# print(df.shape) # 데이터 rows,columns 개수

# print(df['키'].describe())
# print(df['키'].min())
# print(df['키'].max())
# print(df['키'].mean())
# print(df['키'].sum())
# print(df['키'].nlargest()) # 높은 5개, 개수 지정 가능

print(df['SW특기'].count()) # 유효 데이터 수

print(df['학교'].unique()) # 종류
print(df['학교'].nunique()) # 종류의 개수
