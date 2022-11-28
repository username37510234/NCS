import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

plt.title('Bar Graph')

labels = ['강백호','서태웅','정대만']
values = [190,187,184]

# plt.bar(labels,values, color='r')

colors = ['r','g','b']

# plt.bar(labels,values,color=colors, alpha=0.7)

plt.bar(labels,values, width=0.3)
plt.ylim(175,195) # y축 기준값 설정 최소,최대
plt.xticks(rotation=15) # x축 이름을 15도 각도로 표시
plt.yticks(rotation=25) # y축 이름을 25도 각도로 표시

ticks = ['1번학생','2번학생','3번학생']

plt.xticks(labels, ticks)

plt.show()