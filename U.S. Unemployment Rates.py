import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, to_datetime
import ydata_profiling as pp
import seaborn as sns
import warnings
from typing import Union, List, Any, Dict
import os


# Define file paths
df_path = r"D:\USER\Documents\U.S.-Unemployment-Rates\df_sex_unemployment_rates.csv"
dr_path = r"D:\USER\Documents\U.S.-Unemployment-Rates\df_unemployment_rates.csv"

# Read the CSV files into DataFrames
df = pd.read_csv(df_path)
dr = pd.read_csv(dr_path)
df_info = df.info()
dr_info = dr.info()

"""
# EDA for both DataFrames
df_render = pp.ProfileReport(df)
dr_render = pp.ProfileReport(dr)


# Generate HTML reports and save them
df_render.to_file("df_render.html")
dr_render.to_file("dr_render.html")
"""




