import dash
from dash import dcc
from dash import html 

# Create a Dash Application
app = dash.Dash(__name__)

# Define the layout of the Dashboard
app.layout = html.Div(
    children=[
        html.H1('Earnings Dashboard'),
        dcc.Graph(
            id='My-Graph',
            figure={
                'data':[
                    {'x':[1,2,3], 'y':[4,1,2],'type': 'bar', 'name':'Bar chart'},
                    {'x':[1,2,3], 'y':[2,4,5],'type': 'line', 'name':'line chart'},
                ],
                'layout':{
                    'title': 'Graph title',
                    'xaxis': {'title':'x-axis'},
                    'yaxis': {'title':'y-axis'},

                }
            }
        )
    ]
)

# Run the Application
if __name__ == '__main__':
    app.run_server(debug=True)