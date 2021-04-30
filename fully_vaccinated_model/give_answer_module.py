import numpy as np
import API_module

# function three
def answer(df):                                     # take prediction
    minGoal = API_module.population *0.7            # 70% of population is realistic goal (fully vaccinated)
    maxGoal = API_module.population *0.9            # 90% -> unreliastic goal (at the moment)
    minIndex = ''                                   # empty placeholders:
    maxIndex = ''                            
    for value in df["y"]:                           # finds y value instance where this is true ^
        if value >= minGoal:               
            minIndex = df["ds"].index(value)        # returns answer
        elif value == maxGoal: 
            maxIndex = df["ds"].index(value)
    return minIndex, maxIndex                       