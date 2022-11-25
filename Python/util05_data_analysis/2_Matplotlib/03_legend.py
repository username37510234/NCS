import matplotlib.pyplot as plt

plt.title('Line Graph') # 타이틀

x = [1,2,3,4]
y = [2,4,8,16]
plt.plot(x,y, label='data')

# plt.legend() # 범례 등록

# plt.legend(loc='upper right') # 우상단 0~10 숫자로도 지정 가능

# plt.legend(loc=5)

plt.legend(loc=(0.7,0.2))

plt.show()