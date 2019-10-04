#! Try-it-yourself 15-1, 15-2.
import matplotlib.pyplot as pl

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

pl.scatter(x_values, y_values, c=y_values, cmap=pl.cm.Reds,
           edgecolor='none', s=4)

pl.title("Sexy dotes", fontsize=20)
pl.xlabel("Value", fontsize=10)
pl.ylabel("Cubes of velues, 100 bil", fontsize=10)

pl.tick_params(axis='both', which='major', labelsize=14)

pl.axis([0, 5300, 0, 130000000000])

pl.show()
