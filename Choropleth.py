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

latitudes = [32.361538, 58.301935, 33.448457, 34.736009, 38.555605, 39.7391667, 41.767, 39.161921, 30.4518, 33.76,
            21.30895, 43.613739, 39.783250, 39.790942, 41.590939, 39.04, 38.197274, 30.45809, 44.323535, 38.972945,
            42.2352, 42.7335, 44.95,32.320, 38.572954,46.595805,40.809868,39.160949,43.220093, 40.221741,35.667231,
            42.659829,35.771, 48.813343,39.962245, 35.482309,44.931109, 40.269789, 41.82355, 34.000,  44.367966,36.165,
            30.266667,40.7547,44.26639, 37.54, 47.042418,38.349497,43.074722, 41.145548]

longitudes = [-86.279118,-134.419740,-112.073844, -92.331122,-121.468926 ,-104.984167 ,-72.677 , -75.526755 ,
              -84.27277,-84.39,-157.826182 ,-116.237651 ,-89.650373 ,-86.147685 ,-93.620866 ,-95.69 , -84.86311
              ,-91.140229 ,-69.765261 ,-76.501157 ,-71.0275 ,-84.5467 , -93.094 ,-90.207 , -92.189283
              , -112.027031 ,-96.675345 ,-119.753877 ,-71.549127 , -74.756138, -105.964575 , -73.781339 ,-78.638 
              ,-100.779004 ,-83.000647 , -97.534994,-123.029159 ,-76.875613 , -71.422132, -81.035, -100.336378
              ,-86.784 ,-97.75 ,-111.892622 ,-72.57194 ,-77.46 ,-122.893077 ,-81.633294 ,-89.384444 ,-104.802042]
stateAbbreviationList = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND",
"OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")


def dfFormatter(df, selectColumn):
    df_formatted = pd.DataFrame(statesList, columns = ['state'])
    df_formatted['lat'] = latitudes
    df_formatted['long'] = longitudes

    previousDate = "2020-01-01"
    for i in range(len(df['date'])):
        if df['date'][i] != previousDate:
            df_formatted[df['date'][i]] = 0

    df_formatted.set_index('state', inplace=True)

    if selectColumn == 'cases':
 
        for i in range(len(df['state'])):
            df_formatted.loc[df['state'][i], df['date'][i]] = df['cases'][i]

    elif selectColumn == 'deaths':
        for i in range(len(df['state'])):
            df_formatted.loc[df['state'][i], df['date'][i]] = df['deaths'][i]

    df_formatted.reset_index(inplace=True)
    
    df_formatted.drop([50,51,52,53,54], inplace=True)
        
    return df_formatted

nationalcases = dfFormatter(df, 'cases')
nationalcases["state abbreviations"] = stateAbbreviationList

nationaldeaths = dfFormatter(df, 'deaths')
nationaldeaths["state abbreviations"] = stateAbbreviationList

date = input("What date would you like to see COVID-19 data on? ex. 2020-01-21")
colors = ["#cce5ff", "#b3d7ff", "#99caff", "#80bdff", "#66b0ff", "#4da3ff", "#3396ff",
          "#1a88ff", "#007bff", "#006fe6", "#0063cc", "#0056b3", "#004a99", "#003e80", 
          "#003166", "#00254d", "#001933", "#000c1a", "#000000"]
figA = go.Figure(data = go.Choropleth(
    locationmode = "USA-states",
    locations = nationalcases['state abbreviations'],
    z = nationalcases[date],
    colorscale = colors,
    ))
figA.update_layout(
    title_text = "Total Nationwide COVID 19 cases (millions)",
    geo = dict(
        showcoastlines = True, coastlinecolor = "blue",
        scope = "usa"
    )
    ) 
figA.show() 
colors = ["#cce5ff", "#b3d7ff", "#99caff", "#80bdff", "#66b0ff", "#4da3ff", "#3396ff",
        "#1a88ff", "#007bff", "#006fe6", "#0063cc", "#0056b3", "#004a99", "#003e80", 
        "#003166", "#00254d", "#001933", "#000c1a", "#000000"]
figB = go.Figure(data = go.Choropleth(
    locationmode = "USA-states",
    locations = nationaldeaths['state abbreviations'],
    z = nationaldeaths[date],
    colorscale = colors,
    ))
figB.update_layout(
    title_text = "Total Nationwide COVID 19 Deaths (millions)",
    geo = dict(
        showcoastlines = True, coastlinecolor = "blue",
        scope = "usa"
    )
    ) 
figB.show()