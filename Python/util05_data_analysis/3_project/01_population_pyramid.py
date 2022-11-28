import pandas as pd
df_m = pd.read_excel('201112_201112_연령별인구현황_연간.xlsx',skiprows=3,index_col='행정기관',usecols='B,E:Y')

df_m.iloc[0] = df_m.iloc[0].str.replace(',','').astype(int)

df_f = pd.read_excel('201112_201112_연령별인구현황_연간.xlsx',skiprows=3,index_col='행정기관',usecols='B,AB:AV')

df_f.columns = df_m.columns

df_f.iloc[0] = df_f.iloc[0].str.replace(',','').astype(int)

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10,7))
plt.barh(df_m.columns,df_m.iloc[0] // 1000)
plt.barh(df_f.columns,(df_f.iloc[0]* (-1) // 1000))
plt.title('2011 대한민국 인구 피라미드')
plt.legend(loc=(3,0))


plt.savefig('2011_인구피라미드.png', dpi=100)
plt.show()