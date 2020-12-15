import pandas as pd 
import plotly.graph_objects as go

df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")

#print(df.head())
#the data colomuns that we need are: "date", "location" and "positive_rates"
#positive = df["positive_rates"]
#make a dataframe and restructure data 

def datafilter(date1):
    dateFormat = df.loc[df["date"]== date1] 
    data1 = dateFormat.loc[:, ["positive_rate", "location"]]
    return data1
   

def map(fecha):
    #  date1 = input("What date would you like to see positivity rates? (YYYY-MM-DD)")
    #  dateFormat = df.loc[df["date"]== date1] 
    #  df_data = dateFormat.loc[:, ["positive_rate", "location"]]
     #df_better = df_data[df_data.location != 0]
     df_final = datafilter(fecha)
    
     colors =["#FF4D00","#FF6400","#FF7800","#FF8B00","#FF9E00","#FFAE00","#FFD800","#FFE800","#FFF700","#E8FF00","#D8FF00","#C1FF00","#B2FF00","#8BFF00","#2EFF00","#1BFF00","#17FF00","#0CFF00","#00FF0C","#00FF2A","#00FF3E"]

     fig = go.Figure(data = go.Choropleth( 
       locationmode = "country names",
       locations = df_final["location"],
       z = (df_final["positive_rate"])*100,
       colorscale = colors,
       autocolorscale = False,
       reversescale = False, 
       colorbar = dict( nticks = 10),
     ))

     fig.update_layout(
       title_text = " COVID-19 Positive Rates Worldwide")  
     geo = dict(showcoastlines = True)

     return fig.show()
#day = input("What date would you like to see positivity rates for? (YYYY-MM-DD)")
def user(): 
    #string = ""
    #interested = True 
    #while interested == True: 
    day = input("What date would you like to see positivity rates for? (YYYY-MM-DD)")
    #for i in day: 
      #string = day
      #Continue = input("Would you like to keep investigating? please type 'yes' or 'no' ")
      #if Continue.lower() == "yes": 
        #interested = True 
      #else:
        #interested = False
        #break
    return day

def go_on():
  interested = True 
  while interested == True: 
    date = user()
    map(date)
    Continue = input("Would you like to keep investigating? please type 'yes' or 'no' ")
    if Continue.lower() == "yes": 
      interested = True 
    else:
      interested = False
      break


go_on()
