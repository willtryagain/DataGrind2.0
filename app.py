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
# available_indexes = [1]

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
    html.Div([
        dcc.Graph(
            id='crossfilter-indicator-scatter',
            hoverData={'points': [{'customdata': 'Japan'}]}
        )
    ], style={'display': 'inline-block', 'padding': '0 20'}),
])


@app.callback(
    dash.dependencies.Output('crossfilter-indicator-scatter', 'figure'),
    [dash.dependencies.Input('crossfilter-xaxis-column', 'value')])
def update_graph(xaxis_column_name):
    dff = df[df['Index'] == xaxis_column_name]
    fig = px.scatter(x=dff['Date'], y=dff['Volume'])
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)