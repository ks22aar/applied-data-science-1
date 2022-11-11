#!/usr/bin/env python
# coding: utf-8

# In[76]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# data reading
def read_data():
    
    '''Tthis function read data from excel file and return the data'''
    
    # data store in fd variable
    df = pd.read_excel('data.xlsx')
    
    # here function will return the data
    return df
    
 # data manipulation and displaying graph   
def data_reading_and_graphs(df):
    
    '''in this function data is load and data cleaning take place in this function after 
    data cleaning the data show in graphs i used three graphs multiline graph barh graph and pie chart 
    which shows the 5 year data of gdp from 2010 to 2015 
    '''
    # getting  data and and storing in lists
    pakistan = df[df["Countries"]=="Pakistan"]
    
    srilanka = df[df["Countries"]=="Sri Lanka"]
    
    india = df[df["Countries"]=="India"]
    
    bangladesh = df[df["Countries"]=="Bangladesh"]

  
    

    # here we plot the data in the maps its multiline chart
    plt.plot([pakistan["2010"],pakistan["2011"],pakistan["2012"],pakistan["2013"],pakistan["2013"],pakistan["2014"],pakistan["2015"]], label = "Pakistan",)
    
    plt.plot([srilanka["2010"],srilanka["2011"],srilanka["2012"],srilanka["2013"],srilanka["2013"],srilanka["2014"],srilanka["2015"]], label = "Sri Lanka",)
    
    plt.plot([india["2010"],india["2011"],india["2012"],india["2013"],india["2013"],india["2014"],india["2015"]], label = "India",)
    
    plt.plot([bangladesh["2010"],bangladesh["2011"],bangladesh["2012"],bangladesh["2013"],bangladesh["2013"],bangladesh["2014"],bangladesh["2015"]], label = "Bangladesh",)
    
    # here we add legend in the graph
    plt.legend(loc='upper right')
    
    # here we add title in the graph
    plt.title("GDP of South Asian countries")
    
    # here we show graph
    plt.show()
    


    # here we used the bar chart and we are ploting data of pakistan in the bar chart
    objects = ('2010', '2011', '2012', '2013','2014','2015')
    y_pos = np.arange(len(objects))
    
    # here we add pakistan last 5 year data
    performance = [pakistan.iloc[0]["2010"],pakistan.iloc[0]["2011"],pakistan.iloc[0]["2012"],pakistan.iloc[0]["2013"],pakistan.iloc[0]["2014"],pakistan.iloc[0]["2015"]]
    c = ['red', 'yellow', 'black', 'blue', 'orange','green']
    plt.barh(y_pos, performance, align='center', alpha=0.5,color = c)
    plt.yticks(y_pos, objects)
    
    # here we add labels
    plt.xlabel('GDP')
   
    plt.legend(labels=["Pakistan"])
    
    # here we add title
    plt.title('GDP of Pakistan from 2010 to 2015')
    
    # here we ushow graph
    plt.show()
    
    
    objects = ('Pakistan', 'India', 'SriLanka', 'Bangladesh',)
    
    
    y_pos = np.arange(len(objects))
    
    # here we used to calculate the mean of pakistan gdp
    pakistan_mean=my_mean([pakistan.iloc[0]["2010"],pakistan.iloc[0]["2011"],pakistan.iloc[0]["2012"],pakistan.iloc[0]["2013"],pakistan.iloc[0]["2014"],pakistan.iloc[0]["2015"]])
    
    # here we calculate mean on indian gdp
    india_mean=my_mean([india.iloc[0]["2010"],india.iloc[0]["2011"],india.iloc[0]["2012"],india.iloc[0]["2013"],india.iloc[0]["2014"],india.iloc[0]["2015"]])
    
    # here we calculate mean on bangladesh gdp
    bangladesh_mean=my_mean([bangladesh.iloc[0]["2010"],bangladesh.iloc[0]["2011"],bangladesh.iloc[0]["2012"],bangladesh.iloc[0]["2013"],bangladesh.iloc[0]["2014"],bangladesh.iloc[0]["2015"]])
    
    # here we calculate mea on srilanka gdp
    srilanka_mean=my_mean( [srilanka.iloc[0]["2010"],srilanka.iloc[0]["2011"],srilanka.iloc[0]["2012"],srilanka.iloc[0]["2013"],srilanka.iloc[0]["2014"],srilanka.iloc[0]["2015"]])
    
    # here we add all mean data in list
    performance = [pakistan_mean,india_mean,bangladesh_mean,srilanka_mean]
    
    # here we cdefine colors
    c = ['red', 'yellow', 'black', 'blue',]
    
    # here we plot graph
    plt.barh(y_pos, performance, align='center', alpha=0.5,color = c)
    
    plt.yticks(y_pos, objects)
    
    # here we calculate mea on indian gdp
    plt.xlabel('Mean OF GDP')
   
    colors = {'india':'yellow', 'pakistan':'orange','SriLanka':'grey','Bangladesh':'blue'}  
       
    labels = list(colors.keys())
    
    handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
    
    # here we gove bars colors
    plt.legend(handles, labels)
    
    # here we give title
    plt.title('GDP Mean of South Asian Countries')
    
    # here we show graph
    plt.show()

    # here we used the pie chart and we are ploting gdp in 2015 of countries in the pie chart
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    
    # here we Define colors
    colors = ['r', 'y', 'g', 'b']
    
    ax.axis('equal')
    
    # here we set title
    ax.set_title("GDP of South Asian countries in 2015")
    
    
    langs = ['Pakistan', 'Sri Lanka', 'Bangladesh', 'India']
    
    # here we set countries data only for year 2015
    countries_data = [pakistan.iloc[0]["2015"],srilanka.iloc[0]["2015"],bangladesh.iloc[0]["2015"],india.iloc[0]["2015"]]
    
    # here we plot pie chart
    ax.pie(countries_data, labels = langs,colors=colors, 
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
        radius = 1.2, autopct = '%1.1f%%')
    
    # here we set legend
    ax.legend(["pakistan","Sri Lanka","Bangladesh","inda"])
    
    # here we display
    plt.show()
    
    # calculate the mean  
def my_mean(data):
    '''Tthis function read data and calculate the mean and return'''
    return sum(data) / len(data)


# this is mai9n function here we call all functions
if __name__ == "__main__":
         data=read_data()
         data_reading_and_graphs(data)

