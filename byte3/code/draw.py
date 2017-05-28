import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dt

df = pd.read_csv('school_time_re.csv')
df = df.drop(df.columns[[1]],axis=1)

# plot the histogram by date
plt.figure()
plt.bar(df['date'],df['span'])
plt.ylim(ymin=0)
plt.xticks(range(1,19))
plt.xlabel('Date in Feb.')
plt.ylabel('working time (hr)')
plt.title('Working Time in Feburary')
plt.savefig('./working_time.png')
