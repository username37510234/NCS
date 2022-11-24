import pandas as pd
df = pd.read_excel('slam_score.xlsx', index_col='지원번호')

# df.fillna('', inplace=True) # NaN 데이터를 ''으로 채움

import numpy as np

# df['학교'] = np.nan # 학교를 전부 NaN으로

# df.fillna('모름',inplace=True)

# print(df['SW특기'].fillna('확인 중')) # SW특기 중에서 NaN 을 '확인 중' 으로

# df.dropna(inplace=True) # NaN 포함하는 데이터 삭제

df.dropna(axis='index',how='any', inplace=True) # axis = index or columns , how : any or all

print(df)
