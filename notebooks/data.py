from collections import _heapq
import random
import matplotlib.pyplot as plt
import seaborn
import numpy as np
import pandas as pd
from plotly import offline
from plotly.graph_objs import Bar, Layout
import time

# data
"""
squares = np.array([1,4,9,16,25])
cubes = np.array([1,8,27,64,125])

# style data
"""
styles = ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background',
'seaborn-darkgrid', 'seaborn-deep', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale',
'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette',
'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster',
'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

# squares
"""# styling the fig
myStyle = random.choice(styles)
plt.style.use("Solarize_Light2")
print(myStyle)

fig, ax = plt.subplots()

# ploting the data

x_values = range(1,1001,20)
y_values = [y**2 for y in x_values]

ax.scatter(x_values,y_values,c=x_values,s=200,cmap=plt.cm.Blues,linewidth=0.1)

# ax.axis([-50,1050,-(180**2),1050**2])
# ax.scatter(["a","b","c","d","e"], squares, linewidth=5)
# ax.scatter("alp baba",5)

# setting the titles
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Squares", fontsize=19)
ax.set_ylabel("Indices", fontsize=19)

# setting the tick parameters
ax.tick_params(axis="both", which="major", labelsize=9)

plt.show()"""
# cubes
"""
# styling the axes
style = random.choice(styles)
plt.style.use(style)
print(style)

x_values = range(1,5000)
y_values = [i**3 for i in x_values]

# creating the axis
fig, ax = plt.subplots()

# ploting the points
ax.scatter(x_values,y_values, c=x_values, cmap=plt.cm.Greens, linewidth=4)

ax.set_title("Cubes vs Indeces", fontsize=22)
ax.set_xlabel("Indices", fontsize=17)
ax.set_ylabel("Cubes", fontsize=17)

# show the plot
plt.show()"""
# random walk
# molecular motion
"""
class RandomWalk:

    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values) < self.num_points:
            x_direction = random.choice([1])

            x_distance = random.choice([0,1,2,3,4,5,6,7,8])
            x_step = x_direction * x_distance

            y_direction = random.choice([1, -1])

            y_distance = random.choice([0,1,2,3,4,5,6,7,8])
            y_step = y_direction * y_distance

            if not(x_step and y_step):
                self.x_values.append(self.x_values[-1])
                self.y_values.append(self.y_values[-1])
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

rw = RandomWalk(100_000)

rw.fill_walk()

plt.style.use("ggplot")

fig, ax = plt.subplots()
point_numbers = range(rw.num_points)

ax.scatter(rw.x_values, rw.y_values, cmap=plt.cm.Blues, c=point_numbers, s=5,
           edgecolors=None)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

rw1 = RandomWalk()
rw1.fill_walk()

fig1, ax1 = plt.subplots()

ax1.plot(rw1.x_values,rw1.y_values,linewidth=3, c=(0.3,0.7,0.5,0.8))

plt.show()

"""
# pie charts
"""
fig, ax = plt.subplots(figsize=(4,3))
fig1, ax1 = plt.subplots(figsize=(4,3))

style = random.choice(styles)
plt.style.use(style)

ax.pie(squares)
ax1.pie(cubes)

plt.show()
"""
# getting started with plotly (dice example)
"""class Die:

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self,count):
        results = []
        for i in range(count):
            num = random.randint(1,self.num_sides)
            results.append(num)

        return results

roll_start = time.time()
die1 = Die()
die2 = Die()

results1 = die1.roll(10_000)
results2 = die2.roll(10_000)

results = list(map(lambda a,b: a * b,results2,results1))
# max_result = die1.num_sides * die2.num_sides
multipliers = set(i * j for j in range(1,die1.num_sides+1) for i in range(1,die2.num_sides+1))
roll_end = time.time()
print("Roll time: " + str(roll_end - roll_start))

frequencies = []
frequency_start = time.time()

for i in range(1,max_result+1):
    frequency = results.count(i)
    frequencies.append(frequency)

for i in multipliers:
    frequency = results.count(i)
    frequencies.append(frequency)

print(frequencies)
print(multipliers)
frequency_end = time.time()
print("Frequency calculation time: " + str(frequency_end - frequency_start))

plot_start = time.time()
x_values = list(multipliers)

print("list multipliers " + str(list(multipliers)))
data = [Bar(x=x_values,y=frequencies)]
x_axis_config = {"title":"Total Result","dtick":3}
y_axis_config = {"title": "Frequency", "dtick": 200}

my_layout = Layout(title="Results of Rolling D6 and D10 50,000 Times",
                   xaxis=x_axis_config,yaxis=y_axis_config)

offline.plot({"data": data, "layout": my_layout},filename="d6xd6.html")
plot_end = time.time()

print("Plotting time: " + str(plot_end - plot_start))


die1 = Die(8)
die2 = Die(15)
results1 = die1.roll(10_000)
results2 = die2.roll(10_000)

results = list(map(lambda a,b:a + b,results2,results1))
max_result = die1.num_sides + die2.num_sides

frequencies = []
for i in range(2,max_result + 1):
    frequency = results.count(i)
    frequencies.append(frequency)

plt.hist(results,histtype="barstacked")
print(results)
print(frequencies)
plt.show()
"""
# pygal practice
"""
import pygal                                                       # First import pygal
bar_chart = pygal.Bar()                                            # Then create a bar graph object
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
bar_chart.render()
bar_chart.render_to_file('pygal_fibo.svg')                          # Save the svg to a file
"""
# python practice
"""a = "" or "h"
print(a)
def reDefine(arr):
    arr.append(5)
    print(arr)

arr = [9,8,7,6]
print(arr)
reDefine(arr)
print(arr)
print("ğıüİçşö")
print(2 / 3)
n = int(input())
for i in range(n):
    big, small = map(int,input().split())
    divop = 0
    adop = 0
    while big != 0:

        if big == small:
            small += 1
            adop += 1

        if small <= 1:
            adop += 1
            small += 1

        big = big // small
        divop += 1

    print(divop + adop)
"""
# visualizing with csv
"""import math
def reviewsMinusRating(x,rating):
    factor = random.randint(math.ceil(int(x)/15),math.ceil(int(x)/10))
    print("Review: ", x, "Rating: ", rating)
    return x - float(rating)*factor

import csv
from datetime import datetime

with open("books.csv", encoding="utf-8") as f:
    # initializing our variables for the loops
    reader = csv.reader(f)
    reviews, dates, ratings = [], [], []

    # getting the header row
    header_row = next(reader)
    # printing each header with their indices
    for index, header in enumerate(header_row):
        print(index, header.upper())
    # looping through all the file
    for i in reader:
        month = random.randint(1,12)
        day = random.randint(1,28) if month == 2 else random.randint(1,30)
        date = datetime.strptime(f"{day}-{month}-{i[5]}", "%d-%m-%Y")
        dates.append(date)
        reviews.append(int(i[3]))
        ratings.append(i[2])

    scores = list(map(reviewsMinusRating,reviews,ratings))
    print(reviews)
    print(ratings)
    print(dates)
    # print(header_row)
    # print(type(reader))
    # print(next(reader))

global data_amount
data_amount = 520

for i in range(data_amount):
    key = dates[i]
    j = i - 1

    while j >= 0 and dates[j] > key:
        dates[j+1] = dates[j]
        j -= 1

    dates[j+1] = key


plt.style.use("seaborn")

fig, ax = plt.subplots()

ax.plot(dates[:data_amount],reviews[:data_amount], c="g",alpha=0.5)
ax.plot(dates[:data_amount],scores[:data_amount], c="r",alpha=0.5)
ax.fill_between(dates[:data_amount],reviews[:data_amount],scores[:data_amount]
                ,facecolor="yellow",alpha=0.1)

ax.set_title("Reviews of Each Book", fontsize=22)
ax.set_xlabel("",fontsize=16)
ax.set_ylabel("Review Count",fontsize=16)
fig.autofmt_xdate()

ax.tick_params(axis="both",which="major",labelsize=16)
today = datetime.strptime("02/23/2020","%m/%d/%Y")
print(type(today), today)
print(today,dates[0])

# plt.show()
for i in range(10):
    print(i)

    if i == 9:
        print("Too big - I'm giving up!")
        break;
else:
    print("Completed successfully")
"""
# csv visualization practice
import csv
import datetime
import random
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "sanfrasisco.csv"

# istanbul weather 366 data points
with open(filename) as f:
    reader = csv.reader(f)
    headers = next(reader)
    # exploring the headers
    for i, header in enumerate(headers):
        if header == "TMIN":
            minidx = i
        elif header == "TMAX":
            maxidx = i
        elif header == "DATE":
            dateidx = i
        print(i, header.upper())


    dates, rainfalls = [], []
    highs, lows = [], []

    # getting rainfall data
    for row in reader:
        print(row)
        date = datetime.datetime.strptime(row[dateidx],"%Y-%m-%d")
        station = row[1]
        try:
            """if there is data fetch it"""
            # rainfall = float(row[3])
            high = float(row[maxidx])
            low = float(row[minidx])
        except:
            # if there is no data print info
            print(f"Missing data on {date}")
        else:
            """if there is no error append them else don't append"""
            dates.append(date)
            highs.append(high)
            lows.append(low)
            # rainfalls.append(rainfall)


plt.style.use("fivethirtyeight")
plt.xkcd()

fig,ax = plt.subplots()
"""linestyle="", alpha=0.8, marker="","""
"""linestyle="", marker="","""
ax.plot(dates, highs, linewidth=2, c="r", label="High Temp")
ax.plot(dates, lows, linewidth=2, c="b", alpha=0.8, label="Low Temp")

ax.set_title(f"Daily High and Low Temperatures - {dates[0].year}\n{station}", fontsize=21)
ax.set_xlabel("")
ax.set_ylabel("Temperature", fontsize=16)

plt.legend()
fig.autofmt_xdate()

ax.fill_between(dates,highs,lows, alpha=0.1)

ax.tick_params(axis="y",which="minor", length=64.3, width=100, color="red")

# plt.grid(True)
plt.tight_layout()
plt.savefig("xkcd.png")
plt.show()