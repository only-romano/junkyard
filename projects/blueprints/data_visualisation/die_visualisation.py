#! Visualisation of rolling dice
import pygal
from die import Die

# Create a D6.
die = Die()

# Make some rolls and store results in a list.
results = [die.roll() for i in range(1000)]

# Analyze the results.
frequencies = {value: results.count(value) for
               value in range(1, die.num_sides+1)}

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(map(str, [label for label in frequencies.keys()]))
hist.x_title = "Result"
hist.y_title = "Frequence of Result"

hist.add('D6', [value for value in frequencies.values()])
hist.render_to_file('die_visual.svg')
