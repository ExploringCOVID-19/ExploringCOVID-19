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
            
df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv",parse_dates = ['date'])
df_georgia = df.loc[df["state"]=="Georgia"]
df_cases = df_georgia.loc[: , ["date", "cases"]]
df_cases.head()

fig = plt.figure()
ax = fig.add_axes([0,0,2,2]) #[starting poeint on x, starting point on y, lenght, width]
dates = df_cases["date"] #created variable for that column
cases = df_cases["cases"] #created varible for y 
plt.plot(dates, cases)
plt.bar(dates,cases)
plt.xlabel("Dates")
plt.ylabel("Number of Cases (mil)")
plt.title("Cases of COVID-19 Over Time (US)")

#plt.show()
#plt.write_html("covidCases.html", auto_open = True)

def dfFormatter(df, selectColumn):
    #Separate df_formatted from df. Create list of states and their latitudes and longitudes.
    df_formatted = pd.DataFrame(statesList, columns = ['state'])
    df_formatted['lat'] = latitudes
    df_formatted['long'] = longitudes
    
    #Create columns for each date, start off by zeroing out everything.
    #previousDate = datetime.datetime(2020, 1, 1) #Commented out because datetime is no longer a type.
    previousDate = "2020-01-01"
    for i in range(len(df['date'])):
        if df['date'][i] != previousDate:
            df_formatted[df['date'][i]] = 0

    #Set index to states temporarily.
    df_formatted.set_index('state', inplace=True)

    
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
        
    return df_formatted

df_res = pd.read_csv("https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/timeseries/c4_restrictionsongatherings.csv")
df_res.head()
df_impact = df_res.loc[:, ["Unnamed: 0", "01may2020"]]

colors =["#FF4D00","#FF6400","#FF7800","#FF8B00","#FF9E00","#FFAE00","#FFD800","#FFE800","#FFF700","#E8FF00","#D8FF00","#C1FF00","#B2FF00","#8BFF00","#2EFF00","#1BFF00","#17FF00","#0CFF00","#00FF0C","#00FF2A","#00FF3E"]

fig = go.Figure(data = go.Choropleth( 
    locationmode = "country names",
    locations = df_impact["Unnamed: 0"],
    z = df_impact["01may2020"],
    colorscale = colors,
    autocolorscale = False,
    reversescale = False, 
    colorbar = dict(nticks = (int(4))),
))

fig.update_layout(
    title_text = "Level of restrictions for COVID-19 imposed worldwide")  
geo = dict(showcoastlines = True)

fig.show() 
#plt.write_html("covidCases.html", auto_open = True)


def map(date):
  df_impact = df_res.loc[:, ["Unnamed: 0", date]]
  
  colors =["#FF4D00","#FF6400","#FF7800","#FF8B00","#FF9E00","#FFAE00","#FFD800","#FFE800","#FFF700","#E8FF00","#D8FF00","#C1FF00","#B2FF00","#8BFF00","#2EFF00","#1BFF00","#17FF00","#0CFF00","#00FF0C","#00FF2A","#00FF3E"]

  fig = go.Figure(data = go.Choropleth( 
    locationmode = "country names",
    locations = df_impact["Unnamed: 0"],
    z = df_impact[date],
    colorscale = colors,
    autocolorscale = False,
    reversescale = False, 
    colorbar = dict( nticks = 5),

  ))

  fig.update_layout(
    title_text = "Level of restrictions for COVID-19 imposed worldwide")  
  geo = dict(showcoastlines = True)

  #return 
  fig.show()

  map("01jan2020")
