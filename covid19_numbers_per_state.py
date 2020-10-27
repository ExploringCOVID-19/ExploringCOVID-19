LookData = True 
import matplotlib.pyplot as plt
import pandas as pd 
def plot(data,state):
    df_State = df.loc[df["state"]== state]
    df_data = df_State.loc[:,["date", data]]
    fig = plt.figure()                
    # ax = fig.add_axes([.1,.1,.5,1]) #it was too big, so chnage up the numbers .1,.1,.7.7 #add_axes is amethod that takes a list of 4 number where you wanna start x-axis, whre you wanna start on y-axis, and the length and width of figure 
    #[starting point x, starting point y, length, width]
    ax = fig.add_subplot(111)
    dates = df_data["date"] #x values
    data_1 = df_data[data] #y values 
    plt.plot(dates, data_1) #line graph
    plt.bar(dates, data_1) #bar graph
    plt.xlabel("Dates")
    plt.ylabel(data)
    ax.xaxis.set_major_locator(plt.MaxNLocator(6))#displays that many ticks evenly
    plt.title( data + " of COVID-19 Over Time in " + state)
    plt.plot()
    # plt.bar(height = 1, x = 1)
    plt.show() 
df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
# print(df.head())
# print(df.tail())
# Cases_state = input("would you like to see the COVID cases of a specific state, 
while LookData == True:
    data = input("Would you like to look at the deaths or cases for COVID-19?").lower()
    state = input("what state's COVID-19 " + data + " would you like to see?")
    plot(data,state)
    cont_graphs = input("would you like to look at more graphs (type y/n)?").lower()
    if cont_graphs == "y":
        LookData = True
    else:
        LookData = False
        break 
# plot(Cases, New York)
# def plot(data,state):
#     df_State = df.loc[df["state"]== state]
#     df_data = df_State.loc[:,["date", data]]
#     fig = plt.figure()                
#     # ax = fig.add_axes([0, 0, 2, 2]) #it was too big, so chnage up the numbers .1,.1,.7.7 #add_axes is amethod that takes a list of 4 number where you wanna start x-axis, whre you wanna start on y-axis, and the length and width of figure 
#     #[starting point x, starting point y, length, width]
#     ax = fig.add_subplot(111)
#     dates = df_data["date"] #x values
#     data_1 = df_data[data] #y values 
#     plt.plot(dates, data_1) #line graph
#     plt.bar(dates, data_1) #bar graph
#     plt.xlabel("Dates")
#     plt.ylabel(data)
#     ax.xaxis.set_major_locator(plt.MaxNLocator(6))#displays that many ticks evenly
#     plt.title( data + "of COVID-19 Over Time in " + state)
#     plt.plot()
#     plt.bar(height= 1, x = 1)
#     plt.show() 
#     cont_graphs = input("would you like to look at more graphs (type y/n)?").lower()
    