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

nyt_df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")

# Cases function
def plot_cases(state): # defines function
  user_state = nyt_df.loc[nyt_df["state"] == state] # seperates rows based on the state the user enters
  new_df = user_state.loc[: , ['date', 'cases']] #.loc[rows, columns] # the : means "select all"
  fig = plt.figure() # sets the figure
  ax = fig.add_axes([0, 0, 2, 2]) #resizes figure: [starting point x, startng point y, length, width]
  dates = new_df['date'] # x values
  cases = new_df['cases'] # y values

  ax.xaxis.set_major_locator(plt.MaxNLocator(7)) # displays 7 x axis ticks 
  plt.plot(dates, cases) # plots line chart (x, y) 
  plt.bar(dates, cases) # plots bar graph (x, height)
  plt.xlabel("Dates") # displays the x-axis label
  plt.ylabel("Number of Cases") # displays y-axis label
  plt.title("Cases of COVID-19 Over Time (" + state + ")") # displays the title 

  plt.show() # displays the figure alone

# Deaths function
def plot_deaths(state): # defines function
  user_state = nyt_df.loc[nyt_df["state"] == state]  # Seperates rows based on the state the user enters
  new_df = user_state.loc[: , ['date', 'deaths']] #.loc[rows, columns] # the : means "select all"
  fig = plt.figure() # sets the figure
  ax = fig.add_axes([0, 0, 2, 2]) #resizes figure: [starting point x, startng point y, length, width]
  dates = new_df['date'] # x values
  deaths = new_df['deaths'] # y values

  ax.xaxis.set_major_locator(plt.MaxNLocator(7)) # displays 7 x axis ticks 
  plt.plot(dates, deaths) # plots line chart (x, y) 
  plt.bar(dates, deaths) # plots bar graph (x, height)
  plt.xlabel("Dates") # displays the x-axis label
  plt.ylabel("Number of Deaths") # displays y-axis label
  plt.title("Deaths of COVID-19 Over Time (" + state + ")") # displays the title 

  # plt.savefig("barplot.png")
  plt.show() # displays the figure alone

"""Call the functions on your assigned state to visualize the data."""

user_state = str(input("Which state do you want to see the cases and deaths for? "))
plot_cases(user_state)
plot_deaths(user_state)