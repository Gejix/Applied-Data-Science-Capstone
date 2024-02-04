# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("Launch_dash.csv")
geo_df = pd.read_csv("Launch_Geo.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    dcc.Dropdown(id='site-dropdown',
                 options=[
                     {'label': 'All Sites', 'value': 'ALL'},
                     {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                     {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                     {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                     {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}],
                 value='ALL',
                 placeholder="State",
                 searchable=True
                 ),
    html.Br(),
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),
    html.P("Payload range (Kg):"),
    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    marks={0: '0', 100: '100'},
                    value=[min_payload, max_payload]),
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
    html.Br(),
    html.Div(dcc.Graph(id='orbit-bar-chart')),
    html.Br(),
    html.Div(dcc.Graph(id='line-chart')),
])

# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df,
                     values='class',
                     names='Launch Site',
                     title='Total Success Launches By Site',
                     color_discrete_sequence=px.colors.qualitative.Set3)
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        filtered_df = filtered_df.groupby('class').count().reset_index()
        fig = px.pie(filtered_df,
                     values='Unnamed: 0',
                     names='class',
                     title='Total Launches for site {}'.format(entered_site),
                     color_discrete_sequence=px.colors.qualitative.Set3)
    return fig

# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'),
              Input(component_id="payload-slider", component_property="value"))
def get_scatter_chart(entered_site, payload_range):
    if entered_site == 'ALL':
        filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= int(payload_range[0])) &
                                (spacex_df['Payload Mass (kg)'] <= int(payload_range[1]))
                               ]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category', title='All sites - payload mass between {:8,d}kg and {:8,d}kg'.format(int(payload_range[0]), int(payload_range[1])),
                         color_discrete_sequence=px.colors.qualitative.Set3)
    else:
        filtered_df = spacex_df[(spacex_df['Launch Site'] == entered_site) &
                                (spacex_df['Payload Mass (kg)'] >= int(payload_range[0])) &
                                (spacex_df['Payload Mass (kg)'] <= int(payload_range[1]))
                               ]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category', title='Site {} - payload mass between {:8,d}kg and {:8,d}kg'.format(entered_site, int(payload_range[0]), int(payload_range[1])),
                         color_discrete_sequence=px.colors.qualitative.Set3)
    return fig

# Add a callback function for `site-dropdown` as input, `orbit-bar-chart` as output
@app.callback(Output(component_id='orbit-bar-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_bar_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.bar(geo_df.groupby('Orbit')['class'].mean().reset_index(),
                     x='Orbit',
                     y='class',
                     title='Average Success Rate by Orbit',
                     color_discrete_sequence=['green'])
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.bar(filtered_df.groupby('Orbit')['class'].mean().reset_index(),
                     x='Orbit',
                     y='class',
                     title='Average Success Rate by Orbit for site {}'.format(entered_site),
                     color_discrete_sequence=['green'])
    return fig

# Add a callback function for `line-chart`
@app.callback(Output(component_id='line-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_line_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.line(geo_df.groupby('Year')['class'].mean().reset_index(),
                      x='Year',
                      y='class',
                      title='Success Rate Over Time',
                      color_discrete_sequence=['purple'])
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        filtered_df['Year'] = pd.to_datetime(filtered_df['Year']).dt.year
        fig = px.line(filtered_df.groupby('Year')['class'].mean().reset_index(),
                      x='Year',
                      y='class',
                      title='Success Rate Over Time for site {}'.format(entered_site),
                      color_discrete_sequence=['purple'])
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
