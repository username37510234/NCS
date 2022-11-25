import matplotlib.pyplot as plt

plt.title('Line Graph') # 타이틀

x = [1,2,3,4]
y = [2,4,8,16]
plt.plot(x,y)

plt.xlabel('X', color='red')
plt.ylabel('Y', color='#00dd00')

plt.xticks([1,2,3,4])
plt.yticks([3,6,9,12,15])

plt.show()