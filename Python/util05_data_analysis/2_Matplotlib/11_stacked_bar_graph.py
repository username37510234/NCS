import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

plt.title('슬램덩크')

df = pd.read_excel('slam_score.xlsx')

plt.bar(df['이름'],df['국어'],label='국어')
plt.bar(df['이름'],df['영어'],bottom=df['국어'],label='영어')
plt.bar(df['이름'],df['수학'],bottom=df['국어']+df['영어'],label='수학')

plt.xticks(rotation=15)






plt.show()