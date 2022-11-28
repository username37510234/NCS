import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

plt.title('Bar Graph')


labels = ['강백호','서태웅','정대만']
values = [190,187,184]

# plt.barh(labels,values) # 가로 막대 그래프
# plt.xlim(175,195)

bar=plt.bar(labels,values)
# bar[0].set_hatch('/') # 막대안을 / 로 채우기
# bar[1].set_hatch('x') # 막대안을 x 로 채우기
# bar[2].set_hatch('..') # 막대안을 . 로 채우기

for idx,rect in enumerate(bar):
    plt.text(idx, rect.get_height(), values[idx])


plt.show()