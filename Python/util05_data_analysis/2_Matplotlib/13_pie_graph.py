import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

plt.title = "원 그래프"

values = [30,25,20,13,10,2]
labels = ['Python','Java','Javascript','C#','C/C++','ETC']

# plt.pie(values, labels=labels,autopct='%.1f', startangle=90,counterclock=False)

# explode = [0.2,0.1,0,0,0,0]
explode = [0.05] * 6

plt.pie(values, labels=labels,explode=explode)

plt.legend(loc=(1.2,0.3), title="언어별 선호도")




plt.show()