import dash
import dash_html_components as html
import dash_core_components as dcc
import time
import threading
from itertools import cycle

# Create Dash app instance
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1('Running Text'),
    html.Div(id='running-text')
])

# Create a separate function that updates the running text
def update_running_text():
    running_text = "Hello, World!"  # Initial running text
    colors = cycle(['red', 'blue', 'green'])  # Cycle through different colors

    while True:
        color = next(colors)
        running_text = f'<span style="color: {color}">{running_text}</span>'
        time.sleep(1)
        yield running_text

# Create a callback to update the running text
@app.callback(
    dash.dependencies.Output('running-text', 'children'),
    dash.dependencies.Input('running-text', 'id')
)
def update_running_text_div(id):
    return next(update_running_text())

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
