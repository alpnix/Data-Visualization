from plotly.graph_objs import Layout
from plotly.graph_objs import Scatter
from collections import OrderedDict
import plotly.express as px
import pandas as pd
from plotly import offline
import csv

playerFile = "players.csv"
salaryFile = "salaries.csv"

class Player:
    def __init__(self,name=None,draft_year=None,id=None,salary=None,player_id=None):
        self.name = name
        self.draft_year = draft_year
        self.id = id
        self.player_id = player_id
        self.salary = salary


with open(playerFile) as plyr:
    players = []
    plyrReader = csv.reader(plyr)
    plyrHeader = next(plyrReader)
    # print the header
    for i, header in enumerate(plyrHeader):
        print(f"{i} {header.upper()}")


    for player in plyrReader:

        my_player = Player(name=player[20],id=player[0])

        try:
            draft_year = int(player[17])
        except:
            print(f"Missing Data for {my_player.name}")
        else:

            my_player.draft_year = draft_year
            players.append(my_player)


    with open(salaryFile) as slry:
        ids = [i.id for i in players]

        slyrReader = csv.reader(slry)

        slryHeader = next(slyrReader)
        for i, header in enumerate(slryHeader):
            print(f"{i} {header.upper()}")

        for i,player in enumerate(slyrReader):
            player_id = player[1]

            try:
                salary = int(player[2])
            except:
                print(f"Missing data for {player_id}")
            else:
                if player_id in ids:
                    idx = ids.index(player_id)
                    players[idx].salary = salary
                    players[idx].player_id = player_id


# sorting the salary list
def insertionSort(sequence):
    for i in range(len(sequence)):
        key = sequence[i].draft_year
        j = i - 1

        while j >= 0 and sequence[j].draft_year > key:
            sequence[j+1].draft_year = sequence[j].draft_year
            j -= 1

        sequence[j+1].draft_year = key

insertionSort(players)

data = OrderedDict()
avgData = OrderedDict()

for i in players:
    if not(i.salary and i.draft_year):
        continue
    if i.draft_year not in data:
        data[i.draft_year] = [i.salary]
        avgData[i.draft_year] = i.salary
    else:
        data[i.draft_year].append(i.salary)
        seq = data[i.draft_year]
        avgData[i.draft_year] = sum(seq) / len(seq)

print(avgData)
years = avgData.keys()
salaries = avgData.values()
print(type(list(years)), type(salaries))
types = ['area', 'bar', 'barpolar', 'box',
                     'candlestick', 'carpet', 'choropleth',
                     'choroplethmapbox', 'cone', 'contour',
                     'contourcarpet', 'densitymapbox', 'funnel',
                     'funnelarea', 'heatmap', 'heatmapgl',
                     'histogram', 'histogram2d',
                     'histogram2dcontour', 'image', 'indicator',
                     'isosurface', 'mesh3d', 'ohlc', 'parcats',
                     'parcoords', 'pie', 'pointcloud', 'sankey',
                     'scatter', 'scatter3d', 'scattercarpet',
                     'scattergeo', 'scattergl', 'scattermapbox',
                     'scatterpolar', 'scatterpolargl',
                     'scatterternary', 'splom', 'streamtube',
                     'sunburst', 'surface', 'table', 'treemap',
                     'violin', 'volume', 'waterfall']

data = [{
    "type": "histogram",
    "x": list(years),
    "y": list(salaries),
    "hovertext": list(years),
    "hoverinfo": "text + y",
    "marker": {
        "color": "rgb(60,100,150)",
        "line": {
            "width": 4.5,
            "color": "rgb(25,25,25)",
        }
    },
    "opacity": 0.6,
}]
my_layout = {
    "title": "Draft Years vs Average Salaries in the NBA",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Draft Year",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
    "yaxis": {
        "title": "Average Salary",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
}
px.defaults.template = "simple_white"
fig = {"layout": my_layout, "data": data}
offline.plot(fig, filename="graphs/nba-salaries.html")