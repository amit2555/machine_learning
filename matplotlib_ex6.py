#!/usr/bin/python

# Pie Chart

from matplotlib import pyplot as plt

parties = [175000,50000,25000,50000]
labels = ['A','B','C','D']
plt.pie(parties,labels=labels,startangle=90)
plt.show()
