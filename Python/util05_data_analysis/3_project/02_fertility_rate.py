import pandas as pd
df = pd.read_excel('stat_142801.xls',skiprows=2,nrows=2,index_col=0)

df.rename(index={'출생아\xa0수':'출생아 수','합계\xa0출산율':'합계 출산율'},inplace=True)

df = df.T

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False


fig, ax1 = plt.subplots(figsize=(13,5))
ax1.set_ylabel('출생아 수 (천 명)')
ax1.set_ylim(250,700)
ax1.set_yticks([300,400,500,600])
ax1.bar(df.index,df['출생아 수'], color='#ff812d')
for idx,val in enumerate(df['출생아 수']):
    ax1.text(idx, val + 11, val,ha='center')

ax2 = ax1.twinx() # x 축을 공유하는 쌍둥이 axis
ax2.set_ylabel('합계 출산율 (1 명당)')
ax2.set_ylim(0,1.5)
ax2.set_yticks([0,1])
ax2.plot(df.index,df['합계 출산율'], color='#001dff', marker='o', ms=10, linewidth=3,mec='w',mew=1.5)
for idx,val in enumerate(df['합계 출산율']):
    ax2.text(idx, val + 0.08, val,ha='center')


plt.savefig('2012_2021_출산율.png', dpi=100)

plt.show()