import matplotlib.pyplot as plt


plt.title('Line Graph')

x = [1,2,3,4]
y = [2,4,8,16]

plt.plot(x,y)

for idx, txt in enumerate(y):
    plt.text(x[idx],y[idx]+0.3, txt, ha='center',color='blue')
    
plt.show()