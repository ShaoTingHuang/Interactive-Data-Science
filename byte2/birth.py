import os
import jinja2
import logging
import json
import urllib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


df = pd.read_csv('Coffee Production.csv', header = 0)
df = df[3:-3] # filter data

idx = df['EXPORTING COUNTRIES: TOTAL PRODUCTION'].iloc[0:]
df.index = idx.values
df = df[[0,3,4,5,6,7,8]]
del df['EXPORTING COUNTRIES: TOTAL PRODUCTION']

# change data to integer
for k in range(6):
    for i,j in enumerate(df.iloc[:,k]):
        df.iloc[i,k]=int(''.join(re.findall('[0-9]+',j)))

# raw data distribution
for i in range(2, len(df.iloc[:,0])): #exclude world total and member countries
    y = df.iloc[i]
    plt.plot(range(2009,2015),y,label="a")
plt.xlabel('year')
plt.ylabel('coffee production')
plt.title('raw data distribution')
plt.savefig('./raw_data_distribution.png')

# find the principal country and sort by descending
principal = df[df.mean(axis=1) > 5000].sort(['2009 Production'],ascending =False)
principal = principal.drop(['Member countries','Non-member countries'])
word_total = principal.iloc[0,:] # the word total production
principal = principal.iloc[1:,:] # principal country production

# get the other countries' production and combine into the table
others = []
for i in range(len(principal.iloc[0,:])):
    others.append(word_total[i]-sum(principal.iloc[:,i]))
others = pd.DataFrame([others], columns = list(principal))
others=others.set_index([['others']])
principal = principal.append(others)

# plot the production pie chart of the principal country in 2009
plt.figure()
principal['2009 Production'].plot(kind="pie",autopct="%1.1f%%")
plt.title('2009 Production')
plt.ylabel('')
plt.tight_layout()
plt.savefig('./pie.png')

# plot the production pie charts of the principal countries every year
fig = plt.figure()

for j in range(len(principal.iloc[1,:])):
    plt.subplot(2,3,j+1)
    principal[list(principal)[j]].plot(kind="pie",autopct="%1.1f%%", labels = None)
    plt.title(list(principal)[j])
    plt.ylabel('')

plt.legend(principal.index,bbox_to_anchor=(0, 1), loc='upper left', ncol=1, fontsize=10)
plt.tight_layout()
plt.savefig('./pie_years.png')


#print principal.iloc[:,1]
#for i in range(len(principal.iloc[:,0])):

'''
count=[]
for i,j in enumerate(list((set(data['Party'])))):
    count.append(len([k for k in data['Party'] if k==j]))

print(zip(list(set(data['Party'])),count))


plt.pie(count,labels=list((set(data['Party']))))
plt.savefig('./graph.png')

print data
'''
