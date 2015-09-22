#!/ussr/bin/python

from matplotlib import pyplot as plt
from collections import Counter

grades = [99,88,77,66,55,67,78,89,90]
decile = lambda grade: grade //10 *10
histogram = Counter(decile(grade) for grade in grades)

plt.xlabel('Decile')
plt.ylabel('# of Students')
plt.title('Exam Grades')
plt.bar([x-4 for x in histogram.keys()],histogram.values(),8)
plt.axis([-5,110,0,5])
plt.xticks([10*i for i in range(0,11)])
plt.show()

