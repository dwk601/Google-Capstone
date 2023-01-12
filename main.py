import pandas as pd
import glob as glob

rate_data = pd.read_csv('rates.csv')

year_group_data = rate_data.groupby(['Year'])['Effective Federal Funds Rate'].mean()
year_group_data.head()