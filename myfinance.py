"""from mpl_finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas_datareader as web
import datetime as dt

# defining the data interval
start = dt.datetime(2020, 3, 1)
end = dt.datetime.today()
ticker = "MSFT"

# loading in the data
data = web.DataReader(ticker, "yahoo", start, end)

# restructuring the data
data = data[["Open", "High", "Low", "Close"]]

# resetting the index
data.reset_index(inplace=True)

# converting data into seconds(numbers)
data["Date"] = data["Date"].map(mdates.date2num)

# styling the figure
plt.style.use("dark_background")

# graphing the data
fig, ax = plt.subplots()
ax.xaxis_date()
ax.set_axisbelow(True)
ax.set_facecolor("black")
ax.grid(True)

candlestick_ohlc(ax, data.values, width=1,
                 colorup="g", colordown="r", alpha=0.7)

ax.set_title(f"{ticker} Share Price in the Last Year", fontsize=16)
ax.set_xlabel("Dates", fontsize=12)
ax.set_ylabel("Value(USD)", fontsize=12)
fig.autofmt_xdate()
plt.tight_layout()
plt.show()
"""
# live graphs with dash and plotly
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly
import plotly.graph_objs as go
import numpy as np
import datetime as dt
import pandas_datareader as web
from collections import deque
import random

app = dash.Dash()

x = deque(maxlen=10)
y = deque(maxlen=10)
x.append(1)
y.append(1)

app.layout = html.Div(children=[
    html.H1("Dash Practice",style={"textAlign":"center", "margin": "0"}),
    dcc.Input(id="input",autoComplete="off", value="", placeholder="Enter a stock ticker: "),
    html.Div(id="outer-graph"),
    html.Div([
        dcc.Graph(id="live-graph",animate=True),
        dcc.Interval(
            id="graph-update",
            interval=1000,
            n_intervals=0,
        )
    ])

])

# call back is set to integrate the returned value in
# as a child of the div element with outer-graph id
@app.callback(
    Output(component_id="outer-graph",component_property="children"),
    [Input(component_id="input",component_property="value")],
)
# this function runs configured by the callback above
def update_value(input_data):
    stock = input_data.upper()
    # creating a variable so that we can track the last valid
    # stock enterance of the user
    last_working = "MSFT"
    start = dt.datetime(2020, 8, 1)
    end = dt.datetime.now()
    try:
        df = web.DataReader(stock, "yahoo", start, end)
    except:
        df = web.DataReader(last_working, "yahoo", start, end)
        stock = last_working
    else:
        last_working = stock
    df.reset_index(inplace=True)

    # returning the full graph object as a child of
    # div element specified
    return dcc.Graph(id="example-graph",
            figure={
                "data": [{
                    "x": df.Date,
                    "open": df.Open,
                    "high": df.High,
                    "low": df.Low,
                    "close": df.Close,
                    "type": "candlestick",
                    "name": stock
                         }],
                  "layout": {
                      "title": f"{stock} Stock Shares in 2021"
                  }
              }
    )

# figure returning callback bc the element is a graph element
@app.callback(
    Output('live-graph', 'figure'),
    Input('graph-update', 'n_intervals')
)
# appends arbitrary values to x and y deques and then displays them
def live_update_values(n):
    x.append(x[-1] + 1)
    y.append(y[-1]+y[-1] * random.uniform(-0.1,0.1))
    data = plotly.graph_objs.Scatter(
            x=list(x),
            y=list(y),
            name='Scatter',
            mode= 'lines+markers'
    )
    # we will return a figure from this function
    return {'data': [data],
            # range attributes make the ticks dynamically
            # update for both axes
            'layout' : go.Layout(xaxis=dict(
                    range=[min(x),max(x)]),yaxis =
                    dict(range = [min(y),max(y)]),
                    )}



if __name__ == '__main__':
    app.run_server(debug=True)













