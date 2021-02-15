import plotly.express as ps
import pandas as spb

data = spb.read_csv("line_chart.csv")

fig = ps.line(data, x = "Year", y = "Per capita income", color = "Country", title = "Per Capita Income")

fig.show()