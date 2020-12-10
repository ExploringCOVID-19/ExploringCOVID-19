import pandas as pd 
import plotly.graph_objects as go
df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
#the data colomuns that we need are: "date" & "positive_rates"
def user_input():
    user_date = str(input("Which date would you like to see case positivity rates for?: "))
    return user_date
def data(user_date):
    old_df = df[df.location != "World"] # removes "wWorld" row 
    new_df = old_df.loc[df["date"] == user_date]
    positive = new_df["positive_rate"] * 100
    colors = ["#FF4D00", "#FF6400", "#FF7800", "#FF8B00",  "#FF9E00", "#FFAE00", "#FFD800",
            "#FFE800 ", "#FFF700", "#E8FF00", "#D8FF00",  "#C1FF00", "#B2FF00", "#8BFF00",
            "#2EFF00", "#1BFF00", "#17FF00", "#0CFF00",  "#00FF0C", "#00FF2A", "#00FF3E" ] #Hex values
    return new_df, positive, colors
def map(info_list):
    new_df = info_list[0]
    positive = info_list[1]
    colors = info_list[2]
    fig = go.Figure(data = go.Choropleth(
                    locationmode= "country names",
                    locations = new_df["location"],
                    z = positive,
                    colorscale = colors,
                    reversescale = False,
                    autocolorscale = False, #reads our color scale
                    colorbar_title = "Case-positivity rates worldwide (%)",
                    colorbar = dict( nticks = 10)
                    ))            
    fig.update_layout(
    title_text = "Positivity Rates World Choropleth Map",
    geo = dict(
        showcoastlines = True
    )
    )
    fig.write_html("positivityrate.html", auto_open = True)
    