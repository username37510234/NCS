import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

plt.title('슬램덩크')

df = pd.read_excel('slam_score.xlsx')

# plt.plot(df['지원번호'],df['키'])

plt.plot(df['지원번호'],df['영어'])
plt.plot(df['지원번호'],df['수학'])

plt.grid(axis='y', color='purple',alpha=0.3, linestyle="--", linewidth=2) # 격자

plt.show()