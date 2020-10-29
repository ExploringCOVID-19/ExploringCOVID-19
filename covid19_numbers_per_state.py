import pandas
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import matplotlib.ticker as ticker
def plot(data,state):
    df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
#while loop with data types & chloropleth maps to show them
dataType = True 
#possibly need a states list
while dataType:
    statesList = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

    data = input("Would you like to see data on deaths or cases?").lower()
    state = input("Which state would you like to see" + data + "?")
    df_state = df.loc[df['state']== state]
    df_data = df_state.loc[:,["date",data]]
    if dataType == True:
        

