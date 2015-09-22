#!/usr/bin/python

from matplotlib import pyplot as plt

years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2,543.3,1075.9,2862.2,5979.6,10289.7,14958]

plt.plot(years,gdp,marker='o',color='green',linestyle='solid')
plt.xlabel('Year')
plt.ylabel('Billions in $')
plt.title('Nominal GDP')

plt.show()
