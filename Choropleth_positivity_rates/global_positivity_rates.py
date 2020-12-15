import pandas as pd 
import plotly.graph_objects as go

df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
print(df.tail(50))
#the data colomuns that we need are: "date" & "positive_rates"
new_df = df[df.location != "World"]

#make a dataframe and restructure data 

#Use pandas to restructure our data
#Takes totals of each grouped country's # of recoveries for the specified date.
# def dfFormatter(date):
#     total_list = df.groupby('Location')[date].sum().tolist()
#     # print(total_list)
#     country_list = df_2["Location"].tolist()
#     country_set = set(country_list) #sets do not have duplicates
#     country_list = list(country_set)
#     country_list.sort()
#     #new_df2 includes the data we need to generate a choropleth map (UNIQUE country list and total cases for each country)
#     new_df2 = pd.DataFrame(list(zip(country_list2, total_list2)), 
#                 columns =['Country', 'Total_Cases'])
#     new_df2.head()
 def map():
     colors =['#f7fbff','#deebf7','#c6dbef','#9ecae1','#6baed6','#4292c6','#2171b5','#08519c','#08306b'] #Hex values
     fig = go.Figure(data = go.Choropleth( # creates a figure and assigns it to a function that creates a choropleth map
                     locationmode= "country names", # determines the set of locations used to match entries in "locations" parameter
                     locations = new_df["location"], # sets the coordinates via location names(abbreviations)
                     z = new_date["positive rate"], # sets the color values based on the date
                     colorscale = colors, # sets the colorscale based on array of HEX values
                     reversescale = False, # reverses the color mapping if True
                     autocolorscale = False, # reads our color scale
                     colorbar_title = "Global Covid-19 Positivity Rates" # displays title of colorbar 
                     colorbar = dict(nticks = 10)
     ))
     fig.update_layout(
         title_text = "Global Covid-19 Positivity Rates")
         geo = dict( showcoastlines = True )
         fig.show()


  def user_input():
     date = str(input("Which date would you like to look at?: "))


#print(df.head())

#def dfFormatter(date)






