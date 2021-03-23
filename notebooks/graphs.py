import matplotlib.pyplot as plt
import mplcursors
import numpy as np
import pandas as pd
import random
import itertools
import datetime
from collections import *

# 3 bars next to each other
"""width = 0.25

y1_data = np.linspace(1,40,10)
y2_data = np.linspace(1,70,10)
y3_data = np.linspace(1,90,10)

x_data = np.arange(len(y1_data))
plt.xkcd()

fig, ax = plt.subplots()

y1 = x_data - width
y2 = x_data + width

ax.bar(y1,y1_data,width=width,color="blue")
ax.bar(x_data,y2_data,width=width,color="red")
ax.bar(y2,y3_data,width=width,color="green")
ax.set_xticks(ticks=np.arange(0,10,1))
plt.show()"""
# stackplotting 3 players
"""
plt.style.use("fivethirtyeight")

minutes = [1,2,3,4,5,6,7,8,9]
player1 = [1,1,2,2,2,3,4,4,4]
player2 = [1,1,1,2,2,2,2,2,3]
player3 = [1,2,2,2,3,3,4,5,5]

fig, ax = plt.subplots()

ax.stackplot(minutes,player1,player2,player3)

plt.title("Players' Scores Over 3 Minutes")

plt.tight_layout()
plt.show()"""
# histograms
"""plt.style.use("fivethirtyeight")
ages = [18,49,39,19,48,19,19,48,68,19,39,48,9,29,48,38,29]
bins = [10,20,30,40,50,60,70]

plt.hist(ages,bins=bins,edgecolor="black",color="green")
median_age = 29
color = "red"

plt.axvline(median_age,color=color,label="median age")
plt.legend()
plt.show()
"""
# scatter plot with colorbar
"""x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6,2,9,4,5,7,8,7,2])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86,87,94,78,99,86,87,88,111])
colors = np.array([0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
                   60, 65, 70, 75, 80, 85, 90, 95, 100, 110])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()"""
# 3d plots
"""data = pd.read_csv\
    ("D:\Python_Practice\PyDataSci\Data Mining\data\pichici.csv")

fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection="3d")

plot = ax.scatter(data["Goals"],data["Games"],data["Ratio"],
           c=data["Ratio"],cmap="viridis")

ax.set_xlabel("Goals")
ax.set_ylabel("Games")
ax.set_zlabel("Ratio")

cursor = mplcursors.cursor(plot)

def onHover(sel):
    fig.canvas.toolbar.set_message(
        sel.annotation.set_text(list(data["Player"])
                                [int(round(sel.target.index))] +
                                "\n" +
                                list(data["Club"])
                                [int(round(sel.target.index))] +
                                ", " +
                                "{:.2f}".format(data["Ratio"]
                                [int(round(sel.target.index))])
                                )
    )

cursor.connect("add",onHover)

plt.show()
"""
# live data in real time
"""
x_data = []
y_data = []
"""
"""
df = pd.DataFrame(data=[[datetime.now(),0,0,0,0]],
                    columns=["Date","Open","High","Low","Close"])
index = itertools.count()
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].map(mpdates.date2num)


def animate(i):
    plt.style.use('dark_background')
    plt.cla()
    x_data.append(next(index))
    y_data.append(random.randint(-5,5))
    data_points = 15
    start = max(0,len(x_data)-data_points)
    end = max(data_points,len(x_data))
    ax,fig = plt.subplots()
    open = random.random()
    high = max(random.random(),open)
    low = min(random.random(), open)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].map(mpdates.date2num)

    data = {
        "Date": datetime.now(),
        "Open": open,
        "High": high,
        "Low": low,
        "Close": random.uniform(low,high)
    }
    df.append(data,ignore_index=True)
    df.set_index("Date",inplace=True)

    mplfinance.plot(df)

    plt.legend(loc="upper left")
    plt.tight_layout()
    # plt.set_xticks(range(-5,6))

ani = FuncAnimation(plt.gcf(),animate,interval=10000)
# plt.xkcd(*[3,5,5])

plt.show()"""
# huobi api with mpf and plotly
"""
import requests
import json
import pprint
import mplfinance
from matplotlib.animation import FuncAnimation
import mplfinance.plotting as mpf
import matplotlib.dates as mpdates
url = "https://api.huobi.pro/market/history/kline?period=5min&size=3&symbol=btcusdt"
r = requests.get(url)
data = json.loads(r.content)['data']
printer = pprint.PrettyPrinter()
plt.xkcd()
plt.style.use("fivethirtyeight")

reformatted_data = dict()
reformatted_data['Date'] = []
reformatted_data['Open'] = []
reformatted_data['High'] = []
reformatted_data['Low'] = []
reformatted_data['Close'] = []
reformatted_data['Volume'] = []

def animate(i):
    plt.cla()
    r = requests.get(url)
    data = json.loads(r.content)['data']
    for dict in data[::-1]:
        reformatted_data['Date'].append(datetime.datetime.fromtimestamp(dict['id']))
        reformatted_data['Open'].append(dict['open'])
        reformatted_data['High'].append(dict['high'])
        reformatted_data['Low'].append(dict['low'])
        reformatted_data['Close'].append(dict['close'])
        reformatted_data['Volume'].append(dict['vol'])
    print("reformatted data:", reformatted_data)
    pdata = pd.DataFrame.from_dict(reformatted_data)
    pdata.set_index('Date', inplace=True)
    mpf.plot(pdata,type="candle",style="yahoo")


ani = FuncAnimation(plt.gcf(),animate,interval=10000)

plt.show()
import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

df = pd.read_csv('your_file_address')

fig = go.Figure(data=[go.Candlestick(x=df['name_of_time_column'],
                open=df['name_of_open_column'],
                high=df['name_of_high_column'],
                low=df['name_of_low_column'],
                close=df['name_of_close_column'])])

fig.show()"""
# ameritrade api
"""import os
import pprint
import requests

url = f"https://api.tdameritrade.com/v1/instruments"

payload = {
    "apikey": os.getenv("ameritrade"),
    "symbol": "GOOG",
    "projection": "fundamental",
}

printer = pprint.PrettyPrinter()

r = requests.get(url,params=payload)
printer.pprint(r.json())
"""
