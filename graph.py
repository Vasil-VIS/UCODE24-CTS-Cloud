import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

def get_xl(xl):
    if xl<0:
        return xl
    else:
        return -xl


def get_graph(table, k, w):
    t = np.linspace(0, 10, 100)
    y = np.sin(t)

    fig = go.Figure()

    # Define the constants H and w
    H = k*w

    # Define the function y(x)
    def y(x):
        return (H / w) * (np.cosh(w * x / H) - 1)
    
    t_dict = table.T.to_dict()
    x_values_ranges = {}

    for index in range(len(t_dict['XL'])):
        x_values_ranges[t_dict['h'][index]] = np.linspace(abs(t_dict['Xr'][index]), get_xl(t_dict['XL'][index]), 400)

    # Plot each range separately
    for i, (key, x_values) in enumerate(x_values_ranges.items()):
        y_values = y(x_values)
        fig = fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name=key))

    return fig