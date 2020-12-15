import pandas as pd 
import plotly.graph_objects as go
df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
#the data colomuns that we need are: "date" & "positive_rate"

def graph(date_1):
    new_df = df.loc[df["date"]== date_1]
    filtered = new_df.loc[:,["positive_rate", "location"]]
    new_data = filtered[filtered.location != 'World'] #name of coloumn, not equal to 
    colors = ["#FF4D00", "#FF6400", "#FF7800", "#FF8B00",  "#FF9E00", "#FFAE00", "#FFD800",
                "#FFE800 ", "#FFF700", "#E8FF00", "#D8FF00",  "#C1FF00", "#B2FF00", "#8BFF00",
                "#2EFF00", "#1BFF00", "#17FF00", "#0CFF00",  "#00FF0C", "#00FF2A", "#00FF3E" ]
    fig = go.Figure(data = go.Choropleth(
      locationmode = "country names", 
      locations = new_data["location"],
      z = (new_data["positive_rate"]) * 100, #z what data will be represented by the color
      colorscale = colors,
      reversescale = False,
      autocolorscale = False, #gives default patterns
      colorbar = dict(nticks= 10)
      #array = list 
      ))
    fig.update_layout(
      title_text = "Number of COVID-19 Positive Case Rates Worldwide")
    geo = dict(showcoastlines = True)
    fig.show()
    return 
interested = True 
while interested == True:
    date_1 = input("For what date would you like to look at the COVID-19 positivity cases? (YYYY-MM-DD) (starting date is 2020-01-24)")
    date_list = df['date'].tolist()
    check = date_1 in date_list
    if check == True:
        graph(date_1)
        Continue = input("Would you like to keep investigating? please type 'yes' or 'no' ")
        if Continue.lower() == "yes": 
            interested = True 
        else:
            interested = False
            break
    else:
        print("This date is invalid, please enter another one.")