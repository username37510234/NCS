import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [2,4,8,16]
plt.plot(x,y)
plt.title('Line Graph') # 타이틀

import matplotlib
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

import matplotlib.font_manager as fm
fm.fontManager.ttflist # 사용가능 폰트 확인

# plt.title('꺾은선 그래프') 안돼

plt.plot([-1,0,1],[-5,-1,2])

plt.show()