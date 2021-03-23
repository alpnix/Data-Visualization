from matplotlib import pyplot as plt
import matplotlib
"""
import datetime
import random
import math
import csv
filename = "sanfrasisco.csv"

with open(filename) as f:
    reader = csv.reader(f)
    headers = next(reader)

    for i, header in enumerate(headers):
        print(i, header.upper())

    awnds, max_temps = [], []


    for i in reader:
        date = datetime.datetime.strptime(i[5],"%Y-%m-%d")

        try:
            max_temp = int(i[16])
            awnd = float(i[6])

        except:
            print(f"Missing data in {date}")

        else:
            if awnd in awnds:
                continue
            max_temps.append(max_temp)
            awnds.append(awnd)


for i in range(len(awnds)):
    key = awnds[i]
    j = i - 1

    while j >= 0 and awnds[j] > key:
        awnds[j+1] = awnds[j]
        j -= 1

    awnds[j+1] = key

plt.xkcd()

fig, ax = plt.subplots()

# ploting the graph
ax.plot(awnds,max_temps,c="r",linewidth=1,label="Max Temp")
ax.plot(awnds,range(55, len(awnds)+55),c="b",label="Best Fit")

# configuring the axis
ax.set_title("San Fransisco AWND Vs. Max Temp Graph")
ax.set_xlabel("AWND", fontsize=16)
ax.set_ylabel("Max Temp", fontsize=16)

# fig.autofmt_xdate()
plt.legend()
plt.tight_layout()

plt.show()"""
# eartquakes on world map
"""from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import json

# explore the data
filename = "earthquakes.json"
with open(filename,encoding="utf-8") as f:
    all_eq_data = json.load(f)

with open(filename,"w") as f:
    json.dump(all_eq_data,f,indent=4)

all_eq_list = all_eq_data["features"]
mags, lons, lats = [], [], []
print(len(all_eq_list))
for i in all_eq_list:
    mags.append(float(i["properties"]["mag"]))
    lons.append(i["geometry"]["coordinates"][0])
    lats.append(i["geometry"]["coordinates"][1])

# map the earthquakes
data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "marker": {
        "size": [max(0,3*mag) for mag in mags],
    },
}]
my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig,filename="global_eartquakes.html")"""
# one month earthquakes
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from plotly import colors
import json

# explore the data
filename = "monthearthquakes.json"
with open(filename,encoding="utf-8") as f:
    all_eq_data = json.load(f)

with open(filename,"w") as f:
    json.dump(all_eq_data,f,indent=4)

all_eq_list = all_eq_data["features"]
mags, lons, lats, titles = [], [], [], []
print(len(all_eq_list))
for i in all_eq_list:
    title = i["properties"]["title"]
    try:
        mag = float(i["properties"]["mag"])
        lon = i["geometry"]["coordinates"][0]
        lat = i["geometry"]["coordinates"][1]
    except:
        print(f"Missing one data in {title}")
    else:
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        titles.append(title)

# map the earthquakes
data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "text": titles,
    # "name": "Hello World",
    "meta": "sliders",
    "hoverinfo": "text",
    # "hovertemplate": titles,
    # "showlegend": True,
    # "visible": False,
    "marker": {
        # "symbol": "x",
        "size": [max(0,3*mag) for mag in mags],
        "color": mags,
        "colorscale": "Jet",
        # "reversescale": True,
        "colorbar": {"title": "Magnitude"},
    },
}]
my_layout = Layout(title=f"{all_eq_data['metadata']['title']}")

fig = {"data": data, "layout": my_layout}


for key in colors.PLOTLY_SCALES.keys():
    print(key)
print(colors.PLOTLY_SCALES)
offline.plot(fig,filename="graphs/monthly_eartquakes.html")