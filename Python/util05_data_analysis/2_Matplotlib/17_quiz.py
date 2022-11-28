import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows
# matplotlib.rcParams['font.family'] = 'AppleGothic' # Mac
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

data = {
    '영화' : ['명량', '극한직업', '신과함께-죄와 벌', '국제시장', '괴물', '도둑들', '7번방의 선물', '암살'],
    '개봉 연도' : [2014, 2019, 2017, 2014, 2006, 2012, 2013, 2015],
    '관객 수' : [1761, 1626, 1441, 1426, 1301, 1298, 1281, 1270], # (단위 : 만 명)
    '평점' : [8.88, 9.20, 8.73, 9.16, 8.62, 7.64, 8.83, 9.10]
}
df = pd.DataFrame(data)

fig, axs = plt.subplots(3, figsize = (10,10))

axs[0].set_title("국내 Top 8 영화 평점 정보")
axs[0].bar(data['영화'],data['평점'])
axs[0].set(xlabel="영화",ylabel="평점")
axs[0].tick_params(axis='x',rotation=90)

df_group = df.groupby('개봉 연도').mean()

axs[1].plot(df_group.index,df_group['평점'], marker='o')
axs[1].set_ylim([7,10])
axs[1].set_xticks([2005,2010,2015,2020])

filt = df['평점'] >= 9.0
values = [len(df[filt]), len(df[~filt])]
labels = ['9점 이상','9점 미만']

axs[2].pie(values,labels=labels, autopct='%.1f%%')
axs[2].legend(loc=(1,0.3))



plt.show()