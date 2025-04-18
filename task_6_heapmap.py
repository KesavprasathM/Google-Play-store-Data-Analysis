# -*- coding: utf-8 -*-
"""Task 6 Heapmap.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l38VZj1Gx3Hwaqckh_R6dgrPAq4mdWto
"""

# Heatmap: Show the correlation matrix between installs, ratings, and review counts.
#Include only apps updated within the last year, with at least 100,000 installs,
#review count more than 1k, and genres not starting with "A," "F," "E," "G," "I," or "K."
#This graph should be displayed only between 2 PM IST and 4 PM IST.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("cleaned_playstore_data.csv")
data.head()

import pandas as pd

df = pd.read_csv('cleaned_playstore_data.csv')

print("Shape of the DataFrame:", df.shape)
display(df.head())
print(df.info())
print("\nNumber of null values in each column:\n", df.isnull().sum())
print("\nUnique values in 'Category' column:\n", df['Category'].unique())
print("\nUnique values in 'Type' column:\n", df['Type'].unique())
print("\nUnique values in 'Content Rating' column:\n", df['Content Rating'].unique())

from datetime import datetime, timedelta

df['Last Updated'] = pd.to_datetime(df['Last Updated'])

current_date = datetime.now()
one_year_ago = current_date - timedelta(days=365)
df_filtered = df[df['Last Updated'] >= one_year_ago]


df_filtered = df_filtered[df_filtered['Installs'] >= 100000]


df_filtered = df_filtered[df_filtered['Reviews'] > 1000]


prefixes_to_exclude = ['A', 'F', 'E', 'G', 'I', 'K']
df_filtered = df_filtered[~df_filtered['Genres'].str.startswith(tuple(prefixes_to_exclude))]

correlation_matrix = df_correlation.corr()

display(correlation_matrix)

if df_correlation.empty:
  print("df_correlation is empty. Unable to calculate the correlation matrix.")
else:
  correlation_matrix = df_correlation.corr()
  display(correlation_matrix)

from datetime import datetime, timedelta


if df['Last Updated'].dtype == object:
  df['Last Updated'] = pd.to_datetime(df['Last Updated'])

current_date = datetime.now()
two_years_ago = current_date - timedelta(days=365*2)
df_filtered = df[df['Last Updated'] >= two_years_ago]


df_filtered = df_filtered[df_filtered['Installs'] >= 100000]


df_filtered = df_filtered[df_filtered['Reviews'] > 1000]


prefixes_to_exclude = ['A', 'F', 'E', 'G', 'I', 'K']
df_filtered = df_filtered[~df_filtered['Genres'].str.startswith(tuple(prefixes_to_exclude))]

df_correlation = df_filtered[['Installs', 'Rating', 'Reviews']].copy()


print(df_correlation['Installs'].dtype)


if df_correlation['Installs'].dtype == object:
  df_correlation['Installs'] = pd.to_numeric(df_correlation['Installs'], errors='coerce')

if df_correlation.empty:
  print("df_correlation is empty. Unable to calculate the correlation matrix.")
else:
  correlation_matrix = df_correlation.corr()
  display(correlation_matrix)

from datetime import datetime, timedelta


if df['Last Updated'].dtype == object:
  df['Last Updated'] = pd.to_datetime(df['Last Updated'])
current_date = datetime.now()
two_years_ago = current_date - timedelta(days=365*2)
df_filtered = df[df['Last Updated'] >= two_years_ago]

df_filtered = df_filtered[df_filtered['Installs'] >= 50000]

df_filtered = df_filtered[df_filtered['Reviews'] > 500]

prefixes_to_exclude = ['A', 'F', 'E', 'G', 'I', 'K']
df_filtered = df_filtered[~df_filtered['Genres'].str.startswith(tuple(prefixes_to_exclude))]


df_correlation = df_filtered[['Installs', 'Rating', 'Reviews']].copy()

print(df_correlation['Installs'].dtype)


if df_correlation['Installs'].dtype == object:
  df_correlation['Installs'] = pd.to_numeric(df_correlation['Installs'], errors='coerce')

if df_correlation.empty:
  print("df_correlation is empty. Unable to calculate the correlation matrix.")
else:
  correlation_matrix = df_correlation.corr()
  display(correlation_matrix)

from datetime import datetime, timedelta

if df['Last Updated'].dtype == object:
  df['Last Updated'] = pd.to_datetime(df['Last Updated'])

current_date = datetime.now()
two_years_ago = current_date - timedelta(days=365*2)
df_filtered = df[df['Last Updated'] >= two_years_ago]


df_filtered = df_filtered[df_filtered['Installs'] >= 50000]


df_filtered = df_filtered[df_filtered['Reviews'] > 500]



df_correlation = df_filtered[['Installs', 'Rating', 'Reviews']].copy()


print(df_correlation['Installs'].dtype)

if df_correlation['Installs'].dtype == object:
  df_correlation['Installs'] = pd.to_numeric(df_correlation['Installs'], errors='coerce')

if df_correlation.empty:
  print("df_correlation is empty. Unable to calculate the correlation matrix.")
else:
  correlation_matrix = df_correlation.corr()
  display(correlation_matrix)

df_correlation = df[['Installs', 'Rating', 'Reviews']].copy()


df_correlation = df_correlation[df_correlation['Installs'] >= 1000]

if df_correlation.empty:
  print("df_correlation is empty. Unable to calculate the correlation matrix.")
else:
  print(f"df_correlation has {df_correlation.shape[0]} rows.")
  correlation_matrix = df_correlation.corr()
  display(correlation_matrix)



import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import pytz
now_ist=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
if now_ist.hour >= 14 and now_ist.hour <= 16:
 plt.figure(figsize=(8, 6))
 sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
 plt.title('Correlation Matrix of Installs, Ratings, and Review Counts')
 plt.show()
else:
 print("this graph is only displayed only between 2PM and 4PM IST")