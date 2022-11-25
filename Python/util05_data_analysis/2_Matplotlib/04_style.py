import matplotlib.pyplot as plt

plt.title('Line Graph') # 타이틀

x = [1,2,3,4]
y = [2,4,8,16]
# plt.plot(x,y)

# plt.plot(x,y, linewidth=5) # 선 굵기

# plt.plot(x,y, marker='o') # 점표시

# plt.plot(x,y, marker='o', linestyle='None')

# plt.plot(x,y, marker='v', markersize=10)

# plt.plot(x,y, marker='x', markersize=10, markeredgecolor='red')

# plt.plot(x,y, marker='o', markersize=10, markeredgecolor='red',markerfacecolor='yellow')

# plt.plot(x,y, linestyle=':')

# plt.plot(x,y, linestyle='--')

# plt.plot(x,y, linestyle='-.')

# plt.plot(x,y, 'ro--') # color, marker, linestyle 순서대로

# plt.plot(x,y, 'go') # == color='red', marker='o', linestyle='None'

# plt.figure(figsize=(5,10),dpi=200)

plt.figure(facecolor='yellow')

plt.plot(x,y)



plt.show()