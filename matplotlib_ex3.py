#!/usr/bin/python

from matplotlib import pyplot as plt

variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error = [x+y for x,y in zip(variance,bias_squared)]
xs = [i for i,_ in enumerate(variance)]

plt.plot(xs,variance,'r-.',label='variance')
plt.plot(xs,bias_squared,'g-',label='bias_squared')
plt.plot(xs,total_error,'b:',label='total_error')

plt.xlabel('model complexity')
plt.legend(loc='9')
plt.title('Bias-Variance Tradeoff')

plt.show()
