import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")

def choroplethmap(day):
    newdf = df.loc[df["date"] == day]
    newdf2 = newdf.loc[:, ["positive_rate", "location"]]
    newdf3 = newdf2[df.location != "World"]
    colors = ["#cce5ff", "#b3d7ff", "#99caff", "#80bdff", "#66b0ff", "#4da3ff", "#3396ff", 
                "#1a88ff", "#007bff", "#006fe6", "#0063cc", "#0056b3", "#004a99", "#003e80", 
                "#003166", "#00254d", "#001933", "#000c1a","#000000"]
    fig = go.Figure(data=go.Choropleth(
        locationmode = "country names",
        locations = newdf3["location"],
        z = (newdf3["positive_rate"]) * 100,
        colorscale = colors,
        colorbar = dict(nticks=10),
        autocolorscale = False,
        reversescale = False,
        ))
    fig.update_layout(
        title_text = "Global Covid-19 Positivity Rates (millions)",
        geo = dict(
        showcoastlines = True, coastlinecolor = "blue",
        ))
    fig.show()
    return

def day(): 
    date = str(input("Which date would you like to look at? (YYYY-MM-DD) (starting date is 2020-01-24)"))
    date_list = df['date'].tolist()
    check = date in date_list
    if check == True:
        choropleth(date)
     else:
        print("This date is not inside of the data. Please try again.")
        
def contining():
    interested = True
     while interested == True:
        Continue = input("Would you like to see global covid19 data? please type 'yes' or 'no' ")
        if Continue.lower() == "yes":
            day()
        else:
           interested = False
           break
    return interested
