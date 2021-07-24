import pandas as pd
import plotly.express as px
df= pd.read_csv("Covid.csv")
graph=px.scatter(df,x="date", y="cases", color="country")
graph.show()    