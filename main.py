"""from plotly.graph_objs import *
from plotly import offline
import csv
import numpy as np
import matplotlib.pyplot as plt

styles = ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic',
          'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
          'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind',
          'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid',
          'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper',
          'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks',
          'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

student_data = "data/StudentsPerformance.csv"
bio_data = "data/Menstrual Cycle and Ovarian Cycle Graphing.csv"

# extracting data from csv
with open(bio_data) as f:
    reader = csv.reader(f)
    headers = next(reader)
    for i, header in enumerate(headers):
        print(i, header.upper())
    days, fshs, lhs = [], [], []
    estrogens, progesterons = [], []
    for row in reader:
        days.append(int(row[0]))
        fshs.append(int(row[1]))
        lhs.append(int(row[3]))
        estrogens.append(int(row[2]))
        progesterons.append(float(row[4]))

# styling the figure
import random
style = random.choice(styles)
plt.style.use("fivethirtyeight")
plt.style.use('dark_background')

print(style)
# plt.xkcd()

fig, (ax1,ax3) = plt.subplots(2,figsize=(10,8))
color = "tab:red"
ax1.set_xlabel("Days",fontsize=14)
ax1.set_ylabel("FSH Concentration in Blood\n(units/mL)",color=color,fontsize=12)
ax1.plot(days,fshs, color=color, label="FSH")
ax1.set_title("Hormones From The Pituitary",fontsize=20)
ax1.tick_params(axis="y",labelcolor=color)
ax1.legend(loc=2,fontsize=10)

ax2 = ax1.twinx() # create a new axis on the same figure share with same x axis

color = "tab:blue"
ax2.set_ylabel("LH Concentration in Blood\n(units/mL)", color=color,fontsize=12)
ax2.plot(days,lhs, color=color, label="LH")
ax2.tick_params(axis="y",labelcolor=color)
ax2.legend(loc=1,fontsize=10)
ax2.grid(None)


plt.tight_layout()

ax2.grid(None)


color = "tab:red"

ax3.set_xlabel("Days",fontsize=14)
ax3.set_ylabel("Estrogen Concentration in Blood\n(units/mL)",
               color=color, fontsize=12)
D
ax1.set_title("Sex Hormones From Ovary", fontsize=20)
ax1.plot(days, estrogens, color=color, label="Estrogen")
ax1.tick_params(axis="y",color=color)
ax1.legend(loc=2,fontsize=10)

ax3.set_title("Sex Hormones From Ovary", fontsize=20)
ax3.plot(days, estrogens, color=color)
ax3.tick_params(axis="y",labelcolor=color)


ax4 = ax3.twinx()

color = "tab:blue"
ax4.set_ylabel("Progesterone Concentration in Blood\n(units/mL)",
               color=color, fontsize=12)

ax2.plot(days, progesterons, color=color, label="Progesterone")
ax2.tick_params(axis="y",color=color)
ax2.legend(loc=1,fontsize=10)
ax2.grid(None)

ax4.plot(days, progesterons, color=color)
ax4.tick_params(axis="y",labelcolor=color)
ax4.grid(None)

# fig.suptitle("vertical stacked graphs")
ax1.spines["right"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax1.spines["left"].set_visible(False)
ax2.spines["left"].set_visible(False)
ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)
ax1.spines["bottom"].set_visible(False)
ax2.spines["bottom"].set_visible(False)


ax3.spines["right"].set_visible(False)
ax4.spines["right"].set_visible(False)
ax3.spines["left"].set_visible(False)
ax4.spines["left"].set_visible(False)
ax3.spines["top"].set_visible(False)
ax4.spines["top"].set_visible(False)
ax3.spines["bottom"].set_visible(False)
ax4.spines["bottom"].set_visible(False)

plt.suptitle("Hormones in Menstrual Cycle")
plt.tight_layout()

# plt.show()
"""
def reverseList(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.insert(0,arr[i])

    return new_arr

arr = [1,2,3,4,5,6]
arr = reverseList(arr)
print(arr)

"""
from plotly.graph_objs import *
from plotly import offline
import csv
import numpy as np
import matplotlib.pyplot as plt

styles = ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic',
          'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
          'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind',
          'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid',
          'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper',
          'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks',
          'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

student_data = "data/StudentsPerformance.csv"
bio_data = "data/Menstrual Cycle and Ovarian Cycle Graphing.csv"

# extracting data from csv
with open(bio_data) as f:
    reader = csv.reader(f)
    headers = next(reader)
    for i, header in enumerate(headers):
        print(i, header.upper())
    days, fshs, lhs = [], [], []
    estrogens, progesterons = [], []
    for row in reader:
        days.append(int(row[0]))
        fshs.append(int(row[1]))
        lhs.append(int(row[3]))
        estrogens.append(int(row[2]))
        progesterons.append(float(row[4]))

# styling the figure
import random
style = random.choice(styles)
plt.style.use("fivethirtyeight")
print(style)
# plt.xkcd()

fig1, ax1 = plt.subplots()
color = "tab:red"
ax1.set_xlabel("Days",fontsize=14)
ax1.set_ylabel("FSH Concentration in Blood\n(units/mL)",color=color,fontsize=12)
ax1.plot(days,fshs, color=color, label="FSH")
ax1.set_title("Hormones From The Pituitary",fontsize=20)
ax1.tick_params(axis="y",labelcolor=color)
ax1.legend(loc=2,fontsize=10)

ax2 = ax1.twinx() # create a new axis on the same figure share with same x axis

color = "tab:blue"
ax2.set_ylabel("LH Concentration in Blood\n(units/mL)", color=color,fontsize=12)
ax2.plot(days,lhs, color=color, label="LH")
ax2.tick_params(axis="y",labelcolor=color)
ax2.legend(loc=1,fontsize=10)
ax2.grid(None)

plt.tight_layout()

fig2, ax1 = plt.subplots()

color = "tab:red"

ax1.set_xlabel("Days",fontsize=14)
ax1.set_ylabel("Estrogen Concentration in Blood\n(units/mL)",
               color=color, fontsize=12)
ax1.set_title("Sex Hormones From Ovary", fontsize=20)
ax1.plot(days, estrogens, color=color, label="Estrogen")
ax1.tick_params(axis="y",color=color)
ax1.legend(loc=2,fontsize=10)

ax2 = ax1.twinx()

color = "tab:blue"
ax2.set_ylabel("Progesterone Concentration in Blood\n(units/mL)",
               color=color, fontsize=12)
ax2.plot(days, progesterons, color=color, label="Progesterone")
ax2.tick_params(axis="y",color=color)
ax2.legend(loc=1,fontsize=10)
ax2.grid(None)

plt.tight_layout()
plt.show()
"""

class MyList(list):

    def __init__(self):
        pass


alp = MyList()
print(alp.append(5))
print(alp[0])