# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
tls.set_credentials_file(username='KurushDubash', api_key='tj5d0hkqdw')

data = Data([
    Scatter(
        x=[0, 1, 2],
        y=[6, 10, 2],
        error_y=ErrorY(
            type='data',
            array=[1, 2, 3],
            visible=True
        )
    )
])
plot_url = py.plot(data, filename='basic-error-bar')