import matplotlib.pyplot as plt


plt.title('Line Graph')

x = [1,2,3,4]
y = [2,4,8,16]

plt.plot(x,y)

plt.savefig('graph.png', dpi=100)