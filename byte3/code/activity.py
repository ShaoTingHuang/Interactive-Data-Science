import pandas
import datetime
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

df = pandas.read_csv('plugin_ios_activity_recognition.csv',names = ['time_stamp','device_id',\
'activities','confidence','stationary','walking','running',\
'automative','cycling','unknown','label'])
df = df.drop(df.columns[[1,2,3,4,6,7,8,9,10]],axis=1)
df.index = pandas.to_datetime(df.pop('time_stamp'), utc=True)
# change utf-time to datetime
arr = []
with open('plugin_ios_activity_recognition.csv', 'rb') as f:
     reader = csv.reader(f)
     for row in reader:
         arr.append(str(datetime.datetime.fromtimestamp(int(row[1])/1000).strftime('%Y-%m-%d %H:%M:%S')))


df.index = arr
df = df.dropna() #drop nan value
df = df.groupby(df.index).first()
print df.sum()/18759*24
df.plot()
plt.savefig('./walking.png')
