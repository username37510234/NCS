import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False
import pandas as pd
df = pd.read_excel('slam_score.xlsx')

# plt.scatter(df['영어'],df['수학'])
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')

# import numpy as np
# sizes = np.random.rand(8) *1000
# sizes = df['학년'] * 500
z = df['영어']* df['수학']/10
# plt.scatter(df['영어'], df['수학'], s=sizes)
plt.scatter(df['영어'], df['수학'], s=z, c=z ,cmap='viridis',alpha=0.7)
plt.colorbar()

# print(df)


plt.show()