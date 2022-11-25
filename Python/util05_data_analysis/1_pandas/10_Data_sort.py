import pandas as pd
df = pd.read_excel('slam_score.xlsx', index_col='지원번호')

# print(df.sort_values('키'))
# print(df.sort_values('키',ascending=False))
# print(df.sort_values(['수학','영어'],ascending=False))
# print(df.sort_values(['수학','영어'],ascending=[False,True]))

# print(df['키'].sort_values(ascending=False))

print(df.sort_index())