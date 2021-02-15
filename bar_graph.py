import plotly.express as ps
import pandas as spb

data = spb.read_csv("data.csv")

fig = ps.bar(data, x = "Country", y = "InternetUsers", title = "Internet users Per country")

fig.show()