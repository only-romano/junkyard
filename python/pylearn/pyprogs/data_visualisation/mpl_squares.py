#! Testing mathplotlib.
import matplotlib.pyplot as plt

# Pyplot contains a number of functions that help generate charts
# and plots.

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)  # Thickness of the line.

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)    # Title for the chart.
plt.xlabel("Value", fontsize=14)            # Title for the x-axe.
plt.ylabel("Square of Value", fontsize=14)  # Title for the y-axe.

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()
