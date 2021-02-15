import plotly.express as ps
import pandas as spb

data = spb.read_csv("data.csv")

fig = ps.scatter(data, x = "Per capita", y = "Population",size= "Percentage", color = "Country", size_max = 60, title = "Internet users Per country")

fig.show()  