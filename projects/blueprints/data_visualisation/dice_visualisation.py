# Visualisation of several dice.
import pygal
from die import Die

# Create two D6 dice.
die_1, die_2, die_3 = Die(), Die(), Die()

# Make some rolls and store results in a list.
results = [(die_1.roll() + die_2.roll() + die_3.roll()) for i in range(99000)]

# Analyze the results.
frequencies = {value: results.count(value) for
               value in range(3, die_1.num_sides + die_2.num_sides +
                              die_3.num_sides + 1)}

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice 99,000 times."
hist.x_labels = list(map(str, [label for label in frequencies.keys()]))
hist.x_title = "Result"
hist.y_title = "Frequence of Result"

hist.add('D6 + D6 + D6', [value for value in frequencies.values()])
hist.render_to_file('dice_visual2.svg')
