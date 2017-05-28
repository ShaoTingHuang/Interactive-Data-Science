import pandas
import datetime
import numpy as np
import csv
import matplotlib.pyplot as plt

df = pandas.read_csv('aware_debug.csv',names = ['time_stamp','device_id',\
'event','type','label','network','app_version',\
'device','os','battery','battery_state'])

df = df.drop(df.columns[[1,2,3,4,5,6,7,8,10]],axis=1)

df.index = pandas.to_datetime(df.pop('time_stamp'), utc=True)
# change utf-time to datetime
arr = []
with open('aware_debug.csv', 'rb') as f:
     reader = csv.reader(f)
     for row in reader:
         arr.append(str(datetime.datetime.fromtimestamp(int(row[1])/1000).strftime('%Y-%m-%d %H:%M:%S')))

df.index = arr
df = df.dropna() #drop nan value
df = df.groupby(df.index).first()

print df.loc[df['battery'].idxmin()]
#df = df.loc['2017-02-06 1:55:50':'2017-02-06 17:00:00']
#print df['battery'].ix[datetime(2017,02,10,0,0,0):datetime(2017,02,11,0,0,0)]
print df
plt.figure()
df.plot()
plt.savefig('./battery.png')
df.to_csv('battery.csv')
