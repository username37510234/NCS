import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

plt.title = "원 그래프"

colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff']

values = [30,25,20,13,10,2]
labels = ['Python','Java','Javascript','C#','C/C++','ETC']
explode = [0.05]*6
wedgeprops = {'width':0.4, 'edgecolor':'w','linewidth':5}

def custom_autopct(pct):
    # return('%.1f%%' % pct) if pct >= 10 else ''
    return '{:.0f}%'.format(pct) if pct >= 10 else ''

# plt.pie(values, labels=labels,autopct=custom_autopct, startangle=90,counterclock=False, colors=colors, explode=explode,wedgeprops=wedgeprops,pctdistance=0.7)

import pandas as pd
df = pd.read_excel('slam_score.xlsx')

grp = df.groupby('학교')

values = [grp.size()['북산고'],grp.size()['능남고']]
labels = ['북산고','능남고']

plt.title = '소속 학교'
plt.pie(values,labels=labels)


plt.show()