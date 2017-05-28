import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dt


def strToDatetime(s): # utc-time to datetime
    return datetime.strptime(s, '%Y-%m-%d %H:%M:%S')

def roundtohour(d): # datetime to hour
    return round((d.hour + d.minute/60. + d.second/3600.),2)

with open('school_time.csv', 'rb') as f: # read data from file
     data = [row for row in csv.reader(f.read().splitlines())]

arr = [] # change to datetime version
for i in range(len(data)):
    d = strToDatetime(data[i][0].split(',')[0])
    arr.append(d)

# reformate the data
start = []
end = []
for i in range(len(arr)/2):
    start.append(arr[i*2])
    end.append(arr[i*2+1])

# calculate the working hours everyday
df = pd.DataFrame({'arrive': start, 'leave': end})
df['span'] = pd.Series((df['leave'] - df['arrive']))
df.span = pd.Series(round(d.seconds/3600.,2) for d in df['span'])
df.arrive = pd.Series(round((d.hour + d.minute/60. + d.second/3600.),2) for d in df['arrive'])
df.leave = pd.Series(round((d.hour + d.minute/60. + d.second/3600.),2) for d in df['leave'])
df.to_csv('school_time_result.csv')
