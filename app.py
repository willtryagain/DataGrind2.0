from re import X
import dash
from dash import dependencies
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("archive/indexData.csv", parse_dates=["Date"])

available_indexes = df['Index'].unique()
years = [str(year) for year in df['Date'].dt.year.unique()]
years = years[0::5]

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='crossfilter-index',
                options=[{'label': i, 'value': i} for i in available_indexes],
                value='IXIC'
            )
        ],
        style={'padding':'12px 16px'}),
    ],



    style={'padding': '10px 5px'}),

    html.Div(dcc.Slider(
        id='crossfilter-year--slider',
        min=df['Date'].dt.year.min(),
        max=df['Date'].dt.year.max(),
        value=df['Date'].dt.year.max(),
        marks={yr : yr for yr in years},
        step=1
    ), style={'padding': '0px 20px 20px 20px'}),

    html.Div([
        dcc.Graph(
            id='crossfilter-open',
            hoverData={'points': [{'customdata': 'xyz'}]}
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Div([
        dcc.Graph(
            id='crossfilter-high',
            hoverData={'points': [{'customdata': 'xyz'}]}
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Div([
        dcc.Graph(
            id='crossfilter-low',
            hoverData={'points': [{'customdata': 'xyz'}]}
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Div([
        dcc.Graph(
            id='crossfilter-close',
            hoverData={'points': [{'customdata': 'xyz'}]}
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Div([
        dcc.Graph(
            id='crossfilter-adjclose',
            hoverData={'points': [{'customdata': 'xyz'}]}
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Div([
        dcc.Graph(
            id='crossfilter-volume',
            hoverData={'points': [{'customdata': 'xyz'}]}
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

])


@app.callback(
    dash.dependencies.Output('crossfilter-open', 'figure'),
    [dash.dependencies.Input('crossfilter-index', 'value'),
    dash.dependencies.Input('crossfilter-year--slider', 'value')])
def update_graph(xaxis_column_name, year_value):
    dff = df[df['Index'] == xaxis_column_name]
    dff = dff[dff['Date'].dt.year <= year_value]
    fig = px.scatter(dff, x='Date', y="Open")
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    return fig

@app.callback(
    dash.dependencies.Output('crossfilter-high', 'figure'),
    [dash.dependencies.Input('crossfilter-index', 'value'),
    dash.dependencies.Input('crossfilter-year--slider', 'value')])
def update_graph(xaxis_column_name, year_value):
    dff = df[df['Index'] == xaxis_column_name]
    dff = dff[dff['Date'].dt.year <= year_value]
    fig = px.scatter(dff, x='Date', y="High")
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    return fig

@app.callback(
    dash.dependencies.Output('crossfilter-low', 'figure'),
    [dash.dependencies.Input('crossfilter-index', 'value'),
    dash.dependencies.Input('crossfilter-year--slider', 'value')])
def update_graph(xaxis_column_name, year_value):
    dff = df[df['Index'] == xaxis_column_name]
    dff = dff[dff['Date'].dt.year <= year_value]
    fig = px.scatter(dff, x='Date', y="Low")
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    return fig

@app.callback(
    dash.dependencies.Output('crossfilter-close', 'figure'),
    [dash.dependencies.Input('crossfilter-index', 'value'),
    dash.dependencies.Input('crossfilter-year--slider', 'value')])
def update_graph(xaxis_column_name, year_value):
    dff = df[df['Index'] == xaxis_column_name]
    dff = dff[dff['Date'].dt.year <= year_value]
    fig = px.scatter(dff, x='Date', y="Close")
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    return fig


@app.callback(
    dash.dependencies.Output('crossfilter-adjclose', 'figure'),
    [dash.dependencies.Input('crossfilter-index', 'value'),
    dash.dependencies.Input('crossfilter-year--slider', 'value')])
def update_graph(xaxis_column_name, year_value):
    dff = df[df['Index'] == xaxis_column_name]
    dff = dff[dff['Date'].dt.year <= year_value]
    fig = px.scatter(dff, x='Date', y="Adj Close")
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    return fig

@app.callback(
    dash.dependencies.Output('crossfilter-volume', 'figure'),
    [dash.dependencies.Input('crossfilter-index', 'value'),
    dash.dependencies.Input('crossfilter-year--slider', 'value')])
def update_graph(xaxis_column_name, year_value):
    dff = df[df['Index'] == xaxis_column_name]
    dff = dff[dff['Date'].dt.year <= year_value]
    fig = px.scatter(dff, x='Date', y="Volume")
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
