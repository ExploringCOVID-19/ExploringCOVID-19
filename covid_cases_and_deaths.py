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

 #this is a test 
  return plt.plot and plt.bar and  plt.show()

interested = True 
while interested == True:
    data = input("Are you interested in seeing Covid-19 cases or deaths?").lower() #variable for cases or deaths
    more_info = input("Would you like to see a list of all of the states? please type 'yes' or 'no' ").lower()
    if more_info == "yes":
      print(statesList)
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

plt.show()
