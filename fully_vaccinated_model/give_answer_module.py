from fbprophet import Prophet
import pandas as pd 
import matplotlib.pyplot as plot
import numpy as np

#make API calls with python
import requests

#allows us to store results of API call cleanly
import json

#get list of all zipcodes in Los Angeles County separated by commas
laZips = open('laZips.txt', 'r').readlines()
laZips = [z.replace('\n', '') for z in laZips]
laZips = ','.join(laZips)

#put your census API key here
apiKey = "f7038b3e8176fc9358413aad840b9ffbc972a142"

#construct the API call we will use
baseAPI = "https://api.census.gov/data/2017/acs/acs5?key=%s&get=B01003_001E&for=zip%%20code%%20tabulation%%20area:%s" 
calledAPI = baseAPI % (apiKey, laZips)

#call the API and collect the response
response = requests.get(calledAPI)

#load the response into a JSON, ignoring the first element which is just field labels
formattedResponse = json.loads(response.text)[1:]

#flip the order of the response from [population, zipcode] -> [zipcode, population]
formattedResponse = [item[::-1] for item in formattedResponse]

#store the response in a dataframe
laZipPopulations = pd.DataFrame(columns=['zipcode', 'population'], data=formattedResponse)

#save that dataframe to a CSV spreadsheet
csv = laZipPopulations.to_csv('laZipPopulations.csv', index=False)
csv.head()

# function three
def answer(df):                              # take prediction
    population = 332526757                   # temporary population
    minGoal = population *0.7                # 70% of population is realistic goal (fully vaccinated)
    maxGoal = population *0.9                # 90% -> unreliastic goal (at the moment)
    minIndex = ''                            # empty placeholders:
    maxIndex = ''                            
    for value in df["y"]:                    # finds y value instance where this is true ^
        if value >= minGoal:               
            minIndex = df["ds"].index(value) # returns answer
        elif value == maxGoal: 
            maxIndex = df["ds"].index(value)
    return minIndex, maxIndex                