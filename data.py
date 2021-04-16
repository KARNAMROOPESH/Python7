import pandas as pd
import plotly.express as px
data = pd.read_csv("./data.csv")
"""Country,InternetUsers,Population,Per capita,2003,2004,2005,2006,2007,2008,Percenta
 bargraph = px.bar(data,x="Country",y="InternetUsers")
bargraph.show()"""
graph = px.scatter(data,x="Population", y="Per capita", color="Country",size = "Percentage")
graph.show()