import csv
import time
import pandas as pd
import datetime
import numpy as np
import pandas
# read the data from csv to dataframe
df = pandas.read_csv('locations_visit.csv',names = ['time_stamp','device_id', \
'double_latitude','double_longitude','double_arrival','double_departure',\
'address','name','provider','accuracy','label'])
df = df.drop(df.columns[[1,2,3,4,5,7,8,9,10]],axis=1)

df.index = pandas.to_datetime(df.pop('time_stamp'), utc=True)

# change utf-time to datetime
arr = []
with open('locations_visit.csv', 'rb') as f:
     reader = csv.reader(f)
     for row in reader:
         arr.append(str(datetime.datetime.fromtimestamp(int(row[1])/1000).strftime('%Y-%m-%d %H:%M:%S')))
df.index = arr
df = df.dropna() #drop nan value

# get my location frequency
df.address.value_counts().to_csv('map.csv')

df.to_csv('address.csv')
