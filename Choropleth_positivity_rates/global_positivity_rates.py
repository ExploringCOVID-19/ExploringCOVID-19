# The purpose of this script is to map the global positivity rates from February 2020 to the present. There is an animated feature so that users can view the dates across different periods in time. It reads in the data from owid covid data and isolates the columns "positive_rate", "location", and "date" and filters out unwanted data. Then, we use the .choropleth() function from plotly express to display the data with animation.
import pandas as pd
import plotly.express as px
def datafilter():
    df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
    df["positive_rate"] = df["positive_rate"]*100
    newdf = df.loc[:, ["positive_rate", "location", "date"]]
    newdf2 = newdf[df.location != "World"]
    return newdf2
def animatedChoroplethmap():
    our_df = datafilter()
    print("NOTE: Recent data may not be available")
    colors = ['#f7fbff','#deebf7','#c6dbef','#9ecae1','#6baed6','#4292c6','#2171b5','#08519c','#08306b']
    fig = px.choropleth(our_df,
    locationmode= "country names",
    locations = our_df["location"],
    color = "positive_rate", # sets the color values based on the date
    color_continuous_scale = colors, # sets the colorscale based on array of HEX values
    hover_name = our_df["location"],  
    # range_color = [0, 10],
    animation_frame = our_df["date"],
    # colorbar = dict(nticks=10),
    title = "Global Covid-19 Positivity Rates (millions)"
    )
    fig.update_layout(
        # title_text = "Global Covid-19 Positivity Rates (millions)",
        geo = dict(
        showcoastlines = True, coastlinecolor = "blue",
        ))
    fig.write_html("positivityrate.html", auto_open = True)    
# def day(): 
#     date = str(input("Which date would you like to look at? (YYYY-MM-DD) (starting date is 2020-01-24)"))
#     date_list = df['date'].tolist()
#     check = date in date_list
#     if check == True:
#         choroplethmap(date)
#      else:
#         print("This date is not inside of the data. Please try again.")
# def contining():
#     interested = True
#      while interested == True:
#         Continue = input("Would you like to see global covid19 data? please type 'yes' or 'no' ")
#         if Continue.lower() == "yes":
#             day()
#         else:
#            interested = False
#            break
#     return interested
animatedChoroplethmap()