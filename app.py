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
                id='crossfilter-xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indexes],
                value='IXIC'
            )
        ],
        style={'display': 'inline-block'}),

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
            id='crossfilter-indicator-scatter',
            hoverData={'points': [{'customdata': 'xyz'}]}
        )
    ], style={'display': 'inline-block', 'padding': '0 20'}),
])


@app.callback(
    dash.dependencies.Output('crossfilter-indicator-scatter', 'figure'),
    [dash.dependencies.Input('crossfilter-xaxis-column', 'value')])
def update_graph(xaxis_column_name):
    dff = df[df['Index'] == xaxis_column_name]
    fig = px.scatter(dff, x='Date', y="Volume")
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)