# Visualisation of several dice.
import pygal
from die import Die

# Create a D6 and a D10 dice.
die_1 = Die()
die_2 = Die(10)

# Make some rolls and store results in a list.
results = [(die_1.roll() + die_2.roll()) for i in range(1000000)]

# Analyze the results.
frequencies = {value: results.count(value) for
               value in range(1, die_1.num_sides * die_2.num_sides + 1)}

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 dice 50,000 times."
hist.x_labels = list(map(str, [label for label in frequencies.keys()]))
hist.x_title = "Result"
hist.y_title = "Frequence of Result"

hist.add('D6 + D10', [value for value in frequencies.values()])
hist.render_to_file('diferent_dice2.svg')
