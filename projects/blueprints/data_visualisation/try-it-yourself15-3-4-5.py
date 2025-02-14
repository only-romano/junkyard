#! Try-it-yourself
from random import choice
import matplotlib.pyplot as plt


class RandomWalk:

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([i for i in range(0, 9)])
            x_step = x_direction * x_distance
            y_distance = choice([i for i in range(0, 9)])

            if x_step == 0 and y_distance == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_distance
            self.x_values.append(next_x)
            self.y_values.append(next_y)


rw = RandomWalk()
rw.fill_walk()
plt.figure(dpi=100, figsize=(10, 6))

plt.plot(rw.x_values, rw.y_values, c='red')

plt.scatter(0, 0, c='green', edgecolors='none', s=50)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none',
            s=50)

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
