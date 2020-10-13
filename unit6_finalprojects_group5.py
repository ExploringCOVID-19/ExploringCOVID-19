

# Commented out IPython magic to ensure Python compatibility.
#Import all libraries you may need in this cell:
import pandas as pd 
import plotly.graph_objects as go 
import matplotlib.pyplot as plt 
#%matplotlib inline

"""## 1 - Finding the COVID-19 numbers per state."""

#3 lists of data compiled for your convenience

#List of states sorted in alphabetical order.
statesList = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

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
stateAbbreviationList = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND",
"OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
Ask = True 
if Ask == True:
  Cases_state = input("would you like to see the COVID cases of a specific state, enter 'yes' or 'no'?").lower()
  deaths_state = input("would you like to see the COVID deaths  of a specific state, enter 'yes' or 'no'?").lower()
  National 
"""Use the New York Times' COVID-19 data(https://github.com/nytimes/covid-19-data/blob/master/us-states.csv) to create **two functions** that takes the name of a state as input and returns the bar plots of 1) # of cases over time and 2) # of deaths over time for that specific state."""
state = input("what state's COVID-19 cases would you like to see?")
# def covid19(s):
df_State = df.loc[df["state"]== state]
df_data = df_State.loc[:,["date", "cases"]]
fig = plt.figure()                
# ax = fig.add_axes([0, 0, 2, 2]) #it was too big, so chnage up the numbers .1,.1,.7.7 #add_axes is amethod that takes a list of 4 number where you wanna start x-axis, whre you wanna start on y-axis, and the length and width of figure 
#[starting point x, starting point y, length, width]
ax = fig.add_subplot(111)
dates = df_data["date"] #x values
data_1 = df_data["cases"] #y values 

plt.plot(dates, data_1) #line graph
plt.bar(dates, data_1) #bar graph
plt.xlabel("Dates")
plt.ylabel("Cases")
ax.xaxis.set_major_locator(plt.MaxNLocator(6))#displays that many ticks evenly
plt.title("Cases of COVID-19 Over Time in " + state)
plt.plot()
plt.bar(height= 1, x = 1)
plt.show() 
# fig.write_html("fig.html", auto_open=True)


state_d = input("what state's COVID-19 deaths would you like to see?")
df_State = df.loc[df["state"]== state]
df_data = df_State.loc[:,["date", "deaths"]]
fig = plt.figure()                
# ax = fig.add_axes([0, 0, 2, 2]) #add_axes is amethod that takes a list of 4 number where you wanna start x-axis, whre you wanna start on y-axis, and the length and width of figure 
#[starting point x, starting point y, length, width]
dates = df_data["date"] #x values
data_1 = df_data["deaths"] #y values 
ax = fig.add_subplot(111)
plt.plot(dates, data_1) #line graph
plt.bar(dates, data_1) #bar graph
plt.xlabel("Dates")
plt.ylabel("Deaths")
plt.title("Deaths from COVID-19 Over Time in " + state)
ax.xaxis.set_major_locator(plt.MaxNLocator(6))
plt.plot()
plt.bar(height= 1,x = 1)
plt.show()

"""Call the functions on your assigned state to visualize the data."""



"""Use New York Times' COVID-19 data(https://github.com/nytimes/covid-19-data/blob/master/us-states.csv) to create a choropleth map of the United States based on its numbers of COVID-19 cases and deaths. (Use colors that you think are appropriate)."""

#Dataframe Formatter

df = df
selectColumn = input("would you like to see the cases or deaths?").lower()
#Separate df_formatted from df. Create list of states and their latitudes and longitudes.
df_formatted = pd.DataFrame(statesList, columns = ['state']) #a colomun of states
df_formatted['lat'] = latitudes
df_formatted['long'] = longitudes

#Create columns for each date, start off by zeroing out everything.
#previousDate = datetime.datetime(2020, 1, 1) #Commented out because datetime is no longer a type.
previousDate = "2020-01-01" #goes through the date column in org df, a starting point,if it is not equal to jan 1st,2020, it zeroes out evrything 
for i in range(len(df['date'])):
if df['date'][i] != previousDate:
  df_formatted[df['date'][i]] = 0

#Set index to states temporarily.
df_formatted.set_index('state', inplace=True) #instead of making the index numbers, it makes it states


#Select which data you want to use based on the column that you are plotting (cases or deaths)
if selectColumn == 'cases':
#Get number of cases from df and put them in df_formatted.  
for i in range(len(df['state'])):
  df_formatted.loc[df['state'][i], df['date'][i]] = df['cases'][i]
  #Format for .loc : df_formatted.loc['index/row label', 'column label'] = 'value'
elif selectColumn == 'deaths':
for i in range(len(df['state'])):
  df_formatted.loc[df['state'][i], df['date'][i]] = df['deaths'][i]
  #Format for .loc : df_formatted.loc['index/row label', 'column label'] = 'value'


#Reset index when done so that state becomes a column without being the index.
df_formatted.reset_index(inplace=True)

#Drop last 5 rows because we are focusing on the 50 states.
df_formatted.drop([50,51,52,53,54], inplace=True)


#Call the function and assign what it returns to the dataframe variables you will be using.


# def d_c(date, dc): #dc = deaths or cases
df_dc = dfFormatter(df, dc)
date = input("what date would you like to choose in the format y-m-d?")
dc = input("would you like a visualization on the deaths or cases").lower()
colors = ["#FF4D00", "#FF6400", "#FF7800", "#FF8B00",  "#FF9E00", "#FFAE00", "#FFD800",
"#FFE800 ", "#FFF700", "#E8FF00", "#D8FF00",  "#C1FF00", "#B2FF00", "#8BFF00",
"#2EFF00", "#1BFF00", "#17FF00", "#0CFF00",  "#00FF0C", "#00FF2A", "#00FF3E" ]
fig = go.Figure(data = go.Choropleth(
locationmode = "USA-states", 
locations = stateAbbreviationList,
z = df_dc[date], #z repsents the color assignments,  the location, and what data you are accessing
colorscale = colors,
reversescale = False,
autocolorscale = False #gives default patterns
#array = list 
))
fig.update_layout(
title_text = "Number of COVID-19 " + dc + " in USA",
geo = dict(showcoastlines = True, scope = "usa"))
fig.show()



"""## 2 - Analyzing Its Impact on the United States

Group 5 -

The cancellation of public events and gatherings have impacted the world's work-life balance in ways never seen before. Using the following dataset from Oxford University(https://github.com/OxCGRT/covid-policy-tracker/blob/master/data/timeseries/c4_restrictionsongatherings.csv), create a choropleth map of the # of gathering restrictions imposed in each country.
"""



"""## 3 - Challenge (optional): Find a dataset online that explores other ways that COVID-19 has impacted the United States and use pandas and Plotly to create a visualization based on it.

Some ideas:
* number of business closures in each state over time
* number of people telecommuting in the US
* number of hospitalizations in each state

etc..
"""

