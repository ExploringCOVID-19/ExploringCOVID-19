
def datafilter(day):
    newdf = df.loc[df["date"] == day]
    newdf2 = newdf.loc[:, ["positive_rate", "location"]]
    newdf3 = newdf2[df.location != "World"]
    return newdf3
  
def choroplethmap(day):
    datafilter(day)
    colors = ["#cce5ff", "#b3d7ff", "#99caff", "#80bdff", "#66b0ff", "#4da3ff", "#3396ff", 
                "#1a88ff", "#007bff", "#006fe6", "#0063cc", "#0056b3", "#004a99", "#003e80", 
                "#003166", "#00254d", "#001933", "#000c1a","#000000"]
    fig = go.Figure(data=go.Choropleth( # creates a figure and assigns it to a function that creates a choropleth map        locationmode = "country names",
         locations = newdf3["location"],
         z = newdf3["positive rate"] * 100, # sets the color values based on the date
         colorscale = colors, # sets the colorscale based on array of HEX values
         reversescale = False, # reverses the color mapping if True
         autocolorscale = False, # reads our color scale        
         colorbar = dict(nticks=10),
         colorbar_title = "Global Covid-19 Positivity Rates" # displays title of colorbar 
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
        choroplethmap(date)
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