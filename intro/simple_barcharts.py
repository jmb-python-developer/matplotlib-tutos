import numpy as np
from matplotlib import pyplot as plt

# Applies a style
plt.style.use("fivethirtyeight")

# Median Developer Salaries by Age - Generic, no language explicitly declared
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# To plot different data series in bar style, numpy can be used -albeit it might look hacky is what the library provides-
x_indices = np.arange(len(ages_x))
width = 0.25
# With above indices and width, we can add or substract the values of our indices and avoid bars overlapping
# See below calls of plt.bar for both datasets.

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# Uses a 'Bar' type of graphic from here onwards
plt.bar(x_indices - width, dev_y, width=width, color='#444444', label='All Devs')

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indices, py_dev_y, width=width, color='#5a7d9a', linewidth=3, label='Python')

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indices + width, js_dev_y, width=width, color='#CC6CE7', linewidth=3, label='Javascript')

'''
So, this line of code sets the tick marks on the x-axis at the positions specified by x_indices and 
displays the corresponding age labels from ages_x below each tick mark. 
'''
plt.xticks(ticks=x_indices, labels=ages_x)

# Uses a legend
plt.legend()

# Adds titles and legends
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

# Finally, displays plot
plt.show()
