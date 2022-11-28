import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

plt.title('슬램덩크')

df = pd.read_excel('slam_score.xlsx')

import numpy as np

N = df.shape[0]
index = np.arange(N)

w = 0.25
plt.bar(index - w,df['국어'], width=w)
plt.bar(index,df['영어'], width=w)
plt.bar(index + w,df['수학'], width=w)
plt.legend(ncol=3)
plt.xticks(index,df['이름'],rotation=15)




plt.show()