import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, to_datetime
import ydata_profiling as pp
import seaborn as sns
import warnings
from typing import Union, List, Any, Dict
import os
from matplotlib import cm
from matplotlib import colors


# Define file paths
df_path = r"D:\USER\Documents\U.S.-Unemployment-Rates\df_sex_unemployment_rates.csv"
dr_path = r"D:\USER\Documents\U.S.-Unemployment-Rates\df_unemployment_rates.csv"


"""
# EDA for both DataFrames
df_render = pp.ProfileReport(df)
dr_render = pp.ProfileReport(dr)


# Generate HTML reports and save them
df_render.to_file("df_render.html")
dr_render.to_file("dr_render.html")
"""


# Read the CSV files into DataFrames
df = pd.read_csv(df_path) #<------ By sexs 

dr = pd.read_csv(dr_path)#<-------- General/age


#Rows
dr_head = dr.head()
df_head = df.head()

print(df.info(), dr.info())




# Transforming date for get asimilite as a datetime
df['date'] = pd.to_datetime(df['date'])
dr['date'] = pd.to_datetime(dr['date'])


# Calculate the mean overall unemployment rate for men and women
men_mean_rate = df['men_rate'].mean()
women_mean_rate = df['women_rate'].mean()

# Create a figure and axis
plt.figure(figsize=(8, 8))

# Create a pie chart
plt.pie([men_mean_rate, women_mean_rate], labels=['Men', 'Women'], autopct='%1.1f%%', startangle=140)

# Add a title
plt.title('Overall Unemployment Rate Comparison (Men vs. Women)')

# Display the pie chart
plt.show()





#Create a figure and axis
plt.figure(figsize=(15,8))
#Create a plot over time
plt.plot(df['date'], df['men_rate'], label = 'men unemployment rate' , color = 'red' , linewidth=2)
plt.plot(df['date'], df['women_rate'], label = 'women unemployment rate' , color = 'black' , linewidth=2)
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.title('Unemployment Rates for Men vs. Women Over Time')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()



#Create a average unemployment rate 

plt.figure(figsize=(15,8))
plt.plot(dr['date'], dr['overall_rate'], label ='General Unemployment rate' , color = 'black' , linewidth = 2)
plt.xlabel('date') 
plt.ylabel('Unemployment Rate (%)')
plt.title('Unemployment Rates')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()