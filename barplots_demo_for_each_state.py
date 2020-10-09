# creates a function that plots bar graphs that analyze the # of deaths based on age demographics and gender demographics in each state.

#Import all libraries you may need in this cell:
import numpy as np # used to arrange x-axis values for bar plot
import matplotlib.pyplot as plt #to make a visualization
import pandas as pd #to read in csv files and create dataframes
import plotly.graph_objects as go # to create a colorful map visualization 
from matplotlib.dates import DateFormatter #to use matplotlib's date formatter
# %matplotlib inline 
# ^ sets the backend of matplotlib to the 'inline' backend.
# With this backend, the output of plotting commands is displayed inline within frontends like 
# the Jupyter notebook, directly below the code cell that produced it.

#List of states sorted in alphabetical order.
statesList = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

#List of state abbreviations sorted in alphabetical order.
stateAbbreviationList = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND",
"OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

#Corresponding latitudes for each state.
latitudes = [32.361538, 58.301935, 33.448457, 34.736009, 38.555605, 39.7391667, 41.767, 39.161921, 30.4518, 33.76,
            21.30895, 43.613739, 39.783250, 39.790942, 41.590939, 39.04, 38.197274, 30.45809, 44.323535, 38.972945,
            42.2352, 42.7335, 44.95,32.320, 38.572954,46.595805,40.809868,39.160949,43.220093, 40.221741,35.667231,
            42.659829,35.771, 48.813343,39.962245, 35.482309,44.931109, 40.269789, 41.82355, 34.000,  44.367966,36.165,
            30.266667,40.7547,44.26639, 37.54, 47.042418,38.349497,43.074722, 41.145548]

#Corresponding longitudes for each state.
longitudes = [-86.279118,-134.419740,-112.073844, -92.331122,-121.468926 ,-104.984167 ,-72.677 , -75.526755 ,
              -84.27277,-84.39,-157.826182 ,-116.237651 ,-89.650373 ,-86.147685 ,-93.620866 ,-95.69 , -84.86311
              ,-91.140229 ,-69.765261 ,-76.501157 ,-71.0275 ,-84.5467 , -93.094 ,-90.207 , -92.189283
              , -112.027031 ,-96.675345 ,-119.753877 ,-71.549127 , -74.756138, -105.964575 , -73.781339 ,-78.638 
              ,-100.779004 ,-83.000647 , -97.534994,-123.029159 ,-76.875613 , -71.422132, -81.035, -100.336378
              ,-86.784 ,-97.75 ,-111.892622 ,-72.57194 ,-77.46 ,-122.893077 ,-81.633294 ,-89.384444 ,-104.802042]

cdc_df = pd.read_csv("Provisional_COVID-19_Death_Counts_by_Sex__Age__and_State.csv")

def demo_of_deathsPlot(state): # defines function
  user_state = cdc_df.loc[cdc_df["State"]== state] # Seperates rows based on the state the user enters
  female_rows = user_state.loc[user_state["Sex"] == "Female"] # Seperates all female rows
  male_rows = user_state.loc[user_state["Sex"] == "Male"] # # Seperates all male rows

  female_ages = female_rows["Age group"] # stores age groups of females in a variable
  male_ages = male_rows["Age group"] # stores age groups of females in a variable

  female_deaths = female_rows["COVID-19 Deaths"] # stores covid-19 deaths of females in a variable
  male_deaths = male_rows["COVID-19 Deaths"] # stores covid-19 deaths of males in a variable

  fig = plt.figure() # sets the figure
  ax = fig.add_axes([0, 0, 3, 2]) #resizes figure: [starting point x, startng point y, length, width]
  ax.set_ylim(0, (max(female_deaths)+ 5)) # sets y axis limit 0 to maximum values plus 5
  plt.plot(female_ages, female_deaths, label = "Female", color = "pink") # 
  plt.plot(male_ages, male_deaths, label = "Male", color = "cornflowerblue")

  plt.ylabel("Number of Deaths")
  plt.xlabel("ages")
  plt.title(state + "'s COVID-19 deaths by age and gender")

  plt.legend(loc = "upper left")
  plt.show()


def demos_of_deathsBar(state):
  user_state = cdc_df.loc[cdc_df["State"]== state] # Seperates rows based on the state the user enters
  female_rows = user_state.loc[user_state["Sex"] == "Female"] # Seperates all female rows
  male_rows = user_state.loc[user_state["Sex"] == "Male"] # # Seperates all male rows

  female_ages = female_rows["Age group"] # stores age groups of females in a variable
  male_ages = male_rows["Age group"] # stores age groups of females in a variable

  female_deaths = female_rows["COVID-19 Deaths"] # stores covid-19 deaths of females in a variable
  male_deaths = male_rows["COVID-19 Deaths"] # stores covid-19 deaths of males in a variable

  data = [female_deaths, male_deaths] # data variable stores bar data
  X = np.arange(len(female_ages)) # X constant return evenly spaced values within a given interval
  bar_width = 0.35 # variable holds the value of the bar widths

  fig = plt.figure() # sets the figure
  ax = fig.add_axes([0, 0, 2.5, 2])  #resizes figure: [starting point x, startng point y, length, width]
  plt.ylabel("Number of Deaths") # displays the y-axis label
  plt.title(state + "'s COVID-19 deaths by age and gender") # displays the title
  
  ax.bar(X + 0.00, data[0], width = 0.25, color = "pink", label = "Female") # plots female bars
  ax.bar(X + 0.25, data[1], width = 0.25, color = "cornflowerblue", label = "Male") # plots male bars
  plt.xticks(X + bar_width, female_ages)

  plt.legend(loc = "upper center") # displays legend at the top of the figure
  plt.show() # displays figure

user_state = str(input("Which state do you want to see the death bar graphs based on age and gender demographics? "))
demo_of_deathsPlot(user_state)
demos_of_deathsBar(user_state)
