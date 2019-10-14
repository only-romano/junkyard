#! Examine csv
import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Get dates, high & low temperatures from file.
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[16])
            low = int(row[17])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot data.
fig = plt.figure(dpi=115, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)  # Transparency
plt.plot(dates, lows, c='green', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and mean wind speed, Mph - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=13)
fig.autofmt_xdate()     # Draws the date labels diagonally.
plt.ylabel("Wind speed (Mph)", fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=13)

plt.show()
