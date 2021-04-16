import pandas as pd
import plotly.express as px
data = pd.read_csv("./line_chart.csv")
graph = px.line(data, x = "Year", y = "Per capita income", color="Country")
graph.show()