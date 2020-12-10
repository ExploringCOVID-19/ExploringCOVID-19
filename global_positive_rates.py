import pandas as pd
import ploty.graph_objects as go

#make a dataframe and restructure data
df=pd.read("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")

def map(user_date):
    new_df = df.loc[df["date"] == user_date]
    colors = ["#FF4D00", "#FF6400", "#FF7800", "#FF8B00", "#FF9E00", "#FFAE00" , "#FFD800", "FFE800", "#FFF700", "#E8FF00", "#D8FF00", "#C1FF00", "#B2FF00", "#8BFF00", "#2EFF00", "#1BFF00", "#17FF00", "#0CFF00", "#300F0C", "#00FF2A", "#00FF3E"]
    positive = new_df["positive_rate"] * 100
    fig = go.Figure(data = go.choropleth(
                  Locationmode= "country names",
                  locations = new_df["location"]
                  z = positive
                  colorscale = colors,
                  reversescale = False,
                  autocolorscale = False, #reads the color
                  colorbar_title = "Positivity cases rates worldwide %"
                 ))
        fig.update_layout(
      title_text = "Positivy Rates World Map",
      geo = dict(
          showcoastlines = True
        )
        )
        fig.write_html("positivityrate.html",auto_open = True)
def unknown():
    date = str(input("which date would you like to look at?:"))
print(df.head())

old_df = df[df.location != "World"]
new_df = old_df.loc[df["date"] == "2020-6-28"]
print(new_df.tail())

