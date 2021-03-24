import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

games = ['LoL', 'Dota 2', 'CS:GO', 'DayZ', 'HOS', 'Isaac', 'Shows', 'Hearth', 'WoT', 'Agar.io']
viewers = [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

plt.bar(range(len(games)), viewers, color = 'blue')
plt.title('Viewers by Games')
plt.legend(['Twitch'])
plt.xlabel('Games')
plt.ylabel('Viewers')
ax = plt.subplot()
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
ax.set_xticklabels(games, rotation = 30)
plt.show()
plt.clf()

labels = ['US', 'DE', 'CA', 'N/A', 'GB', 'TR', 'BR', 'DK', 'PL', 'BE', 'NL', 'Others']
countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

plt.pie(countries, labels = labels, colors = colors)
plt.legend()
plt.axis('equal')
plt.show()
plt.clf()

hour = range(24)
viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]
y_upper = [i + (i*0.15) for i in viewers_hour]
y_lower = [i - (i*0.15) for i in viewers_hour]

plt.plot(hour, viewers_hour)
plt.fill_between(hour, y_lower, y_upper, alpha = 0.2)
plt.xlabel('Time')
plt.ylabel('Viewers')
plt.title('Viewers by the Hour')
plt.legend()
ax = plt.subplot()
ax.set_xticks(list(range(24)))
plt.show()