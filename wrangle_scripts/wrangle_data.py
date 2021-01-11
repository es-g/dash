import pandas as pd
import plotly.graph_objs as go

def load_data():
    df = pd.read_csv("data/Data.csv")

    return df


