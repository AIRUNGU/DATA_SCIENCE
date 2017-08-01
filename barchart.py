# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 21:25:56 2017

@author: AYUB
"""

from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('rain.csv', sep=',')
print data

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
year = ["Jun", "Feb", "March", "April", "May"]
num_oscars = [5, 11, 3, 8, 10]
# bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]
# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, num_oscars ,color='green')
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")
# label x-axis with movie names at bar centers
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()