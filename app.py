import os
import pathlib
import numpy as np
import pandas as pd
import dash 
from dash import Dash, dcc, html, Input, Output

import plotly.graph_objects as go
import plotly.express as px

import dash_table
from dash_table import DataTable

import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "Manufacturing SPC Dashboard"
server = app.server
app.config["suppress_callback_exceptions"] = True

APP_PATH = str(pathlib.Path(__file__).parent.resolve())
df = pd.read_csv(os.path.join(APP_PATH, os.path.join("data/final", "story.csv")))

params = list(df)
max_length = len(df)

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)