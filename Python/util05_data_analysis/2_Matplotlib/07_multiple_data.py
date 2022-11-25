import matplotlib.pyplot as plt


plt.title('Line Graph')


days = [1,2,3]
az = [2,4,8]
pfizer = [5,1,3]
moderna = [1,2,5]

plt.plot(days, az, label='az')
plt.plot(days, pfizer, label='pfizer', marker='o', linestyle='--')
plt.plot(days, moderna, label='moderna', marker='s', linestyle='-.')
plt.legend(ncol=3)

plt.show()