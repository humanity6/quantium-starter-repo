# importing required libraries
from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px


app = Dash(__name__)
file = open('ProcessedData.csv','r')
df = pd.read_csv(file)

fig = px.line(df,x="date",y="sales",color="region",title="Pink morsel")

app.layout = html.Div(dcc.Graph(id='example-graph',
        figure=fig))

if __name__ == '__main__':
    app.run_server()
