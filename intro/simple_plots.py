from matplotlib import pyplot as plt #Common import convention for this module' class

# Attribute to load presets for styles can be displayed as follows
print(f"Style Presets provided by the library: ${plt.style.available}")

# One a style is chosen, it can be used by invoking the following method of the library
plt.style.use('ggplot')

# Median developer salaries by age - Extracts from StackOverflow data released for 2022.

# Median Developer Salaries by Age - Generic, no language explicitly declared
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# Adding labels and title
plt.title('Median Salary (USD) by Age')
plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

# Third argument is the color of line, but markers can also be used; they both use matplotlib library codes for it.
# Hex values can also be used, see below argument
plt.plot(ages_x, py_dev_y, color='#5a7d9a', marker='o', linewidth=3, label='Python')

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x, js_dev_y, color='#CC6CE7', marker='.', linewidth=3, label='Javascript')

# Above can be plotted as follows, extra arguments for style are added as 3rd, 4th and 5th arguments.
plt.plot(ages_x, dev_y, color='k', linestyle='--', marker='.',label='All Devs')

# Display legends for ALL data series being plotted - labels are added in above .plot() method invocations per data series
plt.legend()

# To display a grid, the following method is called
plt.grid(True)

# To add padding, the following method is called
plt.tight_layout()

# The following saves the plot as a PNG file
plt.savefig('intro/simple-plot-devs-salaries.png')

# Finally, the plot needs to be shown by invoking the following function on the library class
plt.show()