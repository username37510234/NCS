import pandas as pd
df = pd.read_excel('slam_score.xlsx', index_col='지원번호')


# print(df.groupby('학교').get_group('북산고')) # 북산고만 선택

# print(df.groupby('학교').mean()) # 그룹의 평균값

# print(df.groupby('학교').size()) # 각 그룹의 개수

# print(df.groupby('학교').size()['능남고']) # 특정 그룹의 개수

# print(df.groupby('학교')['키'].mean()) # 학교 그룹의 평균 키

# print(df.groupby('학교')[['국어','영어','수학']].mean()) # 학교 그룹의 국어 영어 수학 평균

df['학년'] = [3,3,2,1,1,3,2,2]

# print(df.groupby(['학교','학년']).mean()) # 학교, 학년 별 평균

# print(df.groupby('학년').mean().sort_values('키',ascending=False))

# print(df.groupby(['학교','학년']).sum())

# print(df.groupby('학교')[['이름','SW특기']].count())

school = df.groupby('학교')

print(school['학년'].value_counts().loc['북산고'])