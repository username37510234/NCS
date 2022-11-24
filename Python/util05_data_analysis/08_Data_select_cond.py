import pandas as pd
df = pd.read_excel('slam_score.xlsx', index_col='지원번호')

# print(df['키']>=185)

# filter = (df['키']>=185)

# print(df[filter]) # 필터에 적용되는 대상만 
# print(df[~filter]) # 필터에 적용 안되는 대상만

# print(df.loc[df['키']>=185,'수학']) # 키 185이상(조건)의 수학 데이터(출력물)
# print(df.loc[df['키']>=185,['이름','수학','과학']])

# print(df.loc[(df['키']>=185) & (df['학교'] == '북산고')]) # 키 185이상 이고 학교 북산고

# print(df.loc[(df['키']>200)|(df['키']<170)]) # 키 170미만 이거나 200초과

# filt = df['이름'].str.startswith('송') # 송씨 성을 가진 사람
# print(df[filt])

# filt = df['이름'].str.contains('태') # 이름에 '태'가 들어간 사람
# print(df[filt])
# print(df[~filt])

# langs = ['Python','Java']
# filt = df['SW특기'].isin(langs)
# print(df[filt])

# langs = ["python","java"]
# filt = df['SW특기'].str.lower().isin(langs)
# print(df[filt])

filt = df['SW특기'].str.contains('Java', na=True) # Nan 데이터를 True로 설정, 설정없으면 에러나기도함
print(df[filt])

filt = df['SW특기'].str.contains('Java', na=False) # Nan 데이터를 False로 설정
print(df[filt])