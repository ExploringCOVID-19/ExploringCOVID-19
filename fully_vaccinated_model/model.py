from fbprophet import Prophet #We are working with dataframes and csv files
import pandas as pd # We use pandas libary to read into OWID
from  matplotlib import pyplot as plt #we use pyplot for stylistic purposes 
import numpy as np #some fbprophet uses in our code require np
import data_filter #our module that filters the data into dates (ds column) and fully vaccinated people (y colomun)
import API_module

df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv") #our csv 




def vaccination_rate_prediction(days): # Function that generates predictions for fully vaccinated people 
    new_df = data_filter.US_vaccinated_OWID_filter(df) #new_df is the filtered data fram using the function from the module 
    new_df['cap'] = API_module.population 
    m = Prophet(growth='logistic')
    m.fit(new_df)
    future = m.make_future_dataframe(periods=days)
    future['cap'] = API_module.population 
    future['floor'] = min(new_df["y"])
    forecast = m.predict(future)
    fig = m.plot(forecast)
    plt.title("Fully Vaccinated People in " + str(days) + " days")
    plt.xlabel("Date")
    plt.ylabel("Vaccinated People")
    plt.show()


vaccination_rate_prediction(7)
# vaccination_rate_prediction(30)
# vaccination_rate_prediction(90)
# vaccination_rate_prediction(90 *3)



