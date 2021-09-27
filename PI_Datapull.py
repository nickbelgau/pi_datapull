'''
PI_Datapull
This is a script that pulls data from PI
Developed by: Nick Belgau
'''

import pandas as pd
from datetime import datetime
import time
import pytz
import PIconnect as PI #!pip install PIconnect==0.7


'''User Input'''
tags=['TAG1', 'TAG2'] #Enter tags
pi='INSERT PI SERVER' #Enter PI Server
interval = '15m'
starttime = '01-01-2021 00:00:00'
endtime = '02-01-2021 00:00:00'


'''Find tags on the server'''
server = PI.PIServer(server=pi)
fmt_tags = []   

for tag in tags:
    tag = server.search(tag)   
    fmt_tags.append(tag)
    
tags = fmt_tags
print(tags)

 

'''Datapull'''
marktime = time.time() #starttime
df = pd.DataFrame()

for tag in tags:
    ds = tag[0].interpolated_values(
            starttime,
            endtime,
            interval)
    df2 = pd.DataFrame(ds)      
    if df.empty:
        df = df2
    else:
        df = pd.concat([df,df2],axis=1)

marktime=time.time()-marktime
print(str(df.size) + ' datapoints pulled from ' + str(pi) + ' in ' + str(round(marktime,2)) + ' seconds.')


'''Prepare the DataFrame for timezone conversion'''
df['Datetime'] = df.index
df = df.reset_index()
df = df.drop(df.columns[0],axis=1)
first_col = df.pop('Datetime') #move to first column
df.insert(0,'Datetime',first_col)


'''Convert to PST'''
df = df.astype(str)

for index, row in df.iterrows():
    df['Datetime'][index] = datetime.strptime(df['Datetime'][index], '%Y-%m-%d %H:%M:%S%z')
    df['Datetime'][index] = df['Datetime'][index].astimezone(pytz.timezone('US/Pacific'))

df = df.astype(str)
df['Datetime'] = df['Datetime'].str[:-6] #Remove UTC tagging


'''Inspect data and export'''
print(df.head())

df.to_csv('lots_of_cool_data.csv')