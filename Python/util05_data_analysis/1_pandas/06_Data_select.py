import pandas as pd
df = pd.read_excel('slam_score.xlsx')

# print(df.columns[2] == '학교')

# print(df[df.columns[1]])

# print(df[df.columns[-1]]) # 가장 오른쪽에 있는 정보

# print(df['영어'][0:5])

# print(df[['이름','키']][:3])

print(df[3:])