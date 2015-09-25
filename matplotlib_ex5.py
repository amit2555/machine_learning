#!/usr/bin/python


#Histogram example

from matplotlib import pyplot as plt

age = [21,35,14,3,17,19,31,12,22,8,29,9,4,38,15,32,14,27,9,12,21,33]
bins = [0,10,20,30,40]

plt.hist(age,bins)
plt.show()
