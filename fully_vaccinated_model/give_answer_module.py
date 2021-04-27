import numpy as np
import requests
import json

API = "https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&for=us:*&key=f7038b3e8176fc9358413aad840b9ffbc972a142"

#call the API and collect the response
response = requests.get(API)
#load the response into a JSON, ignoring the first element which is just field labels
formattedResponse = json.loads(response.text)[1:]
population = int(formattedResponse[0][1])

# function three
def answer(df):                                     # take prediction
    population = int(formattedResponse[1][1])       # temporary population
    minGoal = population *0.7                       # 70% of population is realistic goal (fully vaccinated)
    maxGoal = population *0.9                       # 90% -> unreliastic goal (at the moment)
    minIndex = ''                                   # empty placeholders:
    maxIndex = ''                            
    for value in df["y"]:                           # finds y value instance where this is true ^
        if value >= minGoal:               
            minIndex = df["ds"].index(value)        # returns answer
        elif value == maxGoal: 
            maxIndex = df["ds"].index(value)
    return minIndex, maxIndex                