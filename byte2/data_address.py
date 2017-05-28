import csv
import httplib2
from apiclient.discovery import build
import urllib
import json
import os
import jinja2
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

# This API key is provided by google as described in the tutorial
API_KEY = 'AIzaSyCkQ3agqQfj56_Tq8Aa4veZ8LMmmI1E_OM'

# This is the table id for the fusion table
TABLE_ID = '1yJiJwJVa_fNwlK5-RoFvXFCW_ftyt7iDp7pcO9dF'

try:
    fp = open("data.json")
    response = json.load(fp)
except IOError:
    service = build('fusiontables', 'v1', developerKey=API_KEY)
    query = "SELECT * FROM " + TABLE_ID
    response = service.query().sql(sql=query).execute()
    fp = open("data.json", "w+")
    json.dump(response, fp)

df = pd.DataFrame(response[u'rows'], columns = response[u'columns'])

for k in range(2,17):
    for i,j in enumerate(df.iloc[:,k]):
        if df.iloc[i,k] != '':
          df.iloc[i,k]=int(''.join(re.findall('[0-9]+',j)))

# delete the missing data rows
df = df.drop(df.index[[1,8,9,15,17,21,26,29,35,43,48]])

df.index = df['Country'].values
del df['Country']
del df['Coffee Type(s)']

# plot the raw data by year
for i in range(1, len(df.iloc[:,0])):
    y = df.iloc[i]
    plt.plot(range(2000,2015),y,label="a")
plt.xlabel('year')
plt.ylabel('coffee production (bags)')
plt.title('raw data distribution')
plt.savefig('./raw_data_distribution.png')

# plot the total coffee production by year
plt.figure()
plt.plot(range(2000,2015), df.sum())
plt.title('total amount of coffee production by year')
plt.xlabel('year')
plt.ylabel('coffee production (bags)')
plt.savefig('./total_production.png')

# plot the main countries of coffee production by year
main = df[df.mean(axis=1) > 5000]
others = df.sum()-principal.sum()
others = pd.DataFrame([list(others)], columns=list(main))
others = others.set_index([['others']])
main = main.append(others)

plt.figure()
for i in range(len(main.iloc[:,0])):
    y = main.iloc[i]
    plt.plot(range(2000,2015),y,label="a")
plt.xlabel('year')
plt.ylabel('coffee production (bags)')
plt.legend(list(main.index), loc = 1)
plt.title('coffee main producing countries by year')
plt.savefig('./main_countries.png')

# plot pie chart of average production amount of coffee production.
average = main.mean(axis=1)
fig = plt.figure()
average.plot(kind="pie",autopct="%1.1f%%")
plt.title('average production amount of coffee production')
plt.ylabel('')
plt.tight_layout()
plt.savefig('./pie.png')

# plot main countries of coffee production boxplot
plt.figure()
sns.boxplot(main.transpose())
plt.xlabel('countries')
plt.ylabel('year production')
plt.title('countries production boxplot')
