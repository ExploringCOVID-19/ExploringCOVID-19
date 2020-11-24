import pandas as pd 
import plotly.graph_objects as go

df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
print(df.tail(50))
#the data colomuns that we need are: "date" & "positive_rates"
positive = df["positive_rates"]
#make a dataframe and restructure data 
