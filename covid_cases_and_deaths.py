import pandas as pd 
import plotly.graph_objects as go 
import matplotlib.pyplot as plt 

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

df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
# this is a test 
def typo(word): 
  placeholder = ""
  for i in word: 
    placeholder = i 
  if placeholder == " ":
    fixedword = word[0:len(word) -1]
    return fixedword
  return word
    

def plot(data,state):
  df_State = df.loc[df["state"]== state]
  df_data = df_State.loc[:,["date", data]]
  fig = plt.figure()                
  ax = fig.add_subplot(111) #add_axes is amethod that takes a list of 4 number where you wanna start x-axis, whre you wanna start on y-axis, and the length and width of figure 
#[starting point x, starting point y, length, width]
  dates = df_data["date"] #x values
  data_1 = df_data[data] #y values 

  plt.plot(dates, data_1) #line graph
  plt.bar(dates, data_1) #bar graph
  plt.xlabel("Dates")
  plt.ylabel(data)
  ax.xaxis.set_major_locator(plt.MaxNLocator(5))#displays that many ticks evenly
  plt.title(data + " of COVID-19 Over Time in " + state)

 
  return plt.plot and plt.bar and  plt.show()

interested = True 
while interested == True:
    data = input("Are you interested in seeing Covid-19 cases or deaths?").lower() #variable for cases or deaths 
    state = input("What state do you want to see Covid-19 " + data + " for?") # variable for state
    fixeddata = typo(data)
    fixedstate = typo(state)
    plot(fixeddata,fixedstate)
    Continue = input("Would you like to keep investigating? please type 'yes' or 'no' ")
    if Continue.lower() == "yes": 
     interested = True 
    else:
     interested = False
     break



#covid19("New York")    

#def covid19_deaths(state):
  #df_State = df.loc[df["state"]== state]
 # df_data = df_State.loc[:,["date", "deaths"]]
  #fig = plt.figure()                
  #ax = fig.add_subplot(111) #add_axes is amethod that takes a list of 4 number where you wanna start x-axis, whre you wanna start on y-axis, and the length and width of figure 
#[starting point x, starting point y, length, width]
  #dates = df_data["date"] #x values
  #data_1 = df_data["deaths"] #y values 

  #plt.plot(dates, data_1) #line graph
  #plt.bar(dates, data_1) #bar graph
  #plt.xlabel("Dates")
  #plt.ylabel("Deaths")
  #plt.title("Deaths from COVID-19 Over Time in " + state)
  #ax.xaxis.set_major_locator(plt.MaxNLocator(5))
  #return plt.plot and plt.bar and  plt.show()
#covid19_deaths("New York")