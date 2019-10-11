# Visualisation of random_walk.py
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk, and plot the points.
rw = RandomWalk(50000)
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Reds, s=5)
plt.show()

# Keep making new walks as long as the program is actiove.
while True:
    # Make a random walk and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(dpi=168, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greys,
                edgecolor='none', s=1)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='blue', edgecolors='none', s=25)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=25)

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
