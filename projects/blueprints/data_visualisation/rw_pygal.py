# Visualisation of random_walk.py
import pygal
from random_walk import RandomWalk

# Make a random walk, and plot the points.
rw = RandomWalk(10000)
rw.fill_walk()

hist = pygal.Bar()

hist.title = "Random walk."
hist.x_labels = rw.x_values
hist.x_title = "X"
hist.y_title = "Y"

hist.add('Random walk', rw.y_values)
hist.render_to_file('rw.svg')
