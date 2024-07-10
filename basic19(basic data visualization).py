import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,5,7,11]

plt.plot(x, y, marker = 'o', linestyle = '--', color='b', label='Prime Numbers' )

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('prime numbers plot')

plt.legend()

plt.show()

import seaborn as sns

tips = sns.load_dataset('tips')
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex', style='time')

plt.xlabel('total bill')
plt.ylabel('tip')
plt.title('tip analysis')

plt.show()