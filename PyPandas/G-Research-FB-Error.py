
# coding: utf-8

# In[60]:

import os
import numpy as np
import pandas as pd
import pickle
from datetime import datetime
from dateutil.parser import parse
from itertools import chain
import operator
import sys
from fbprophet import Prophet
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.offline as py

from fbprophet import Prophet
from pandas.tseries.offsets import *
#py.init_notebook_mode(connected=True)
#get_ipython().magic('matplotlib inline')



# In[61]:


import plotly.graph_objs as go
import plotly.figure_factory as ff
py.init_notebook_mode(connected=True)


# In[62]:

df_result = pd.read_csv("output/df_result_fb.csv")


# In[63]:

#run it against a small population
#df_result = df_result[(df_result.Stock == 830)|(df_result.Stock == 828)|(df_result.Stock == 363)|(df_result.Stock == 1223)|(df_result.Stock == 1372)]
#df_result = df_result[(df_result.Stock == 363)]
#df_result = df_result[(df_result.Stock == 1797)]
df_result.rename(columns={'Unnamed: 0': 'Pop', 'Unnamed: 1': 'Count'}, inplace=True)
df_result['ds']=pd.to_datetime(df_result['FB_Date'], format='%Y-%m-%d')
df_result.head()


# In[64]:

def run_fb(row):
    Market = row['Market']
    Stock = row['Stock']
    period = row['count']
    #Step 1 get the dataframe for the Market and Security from df
    df_train=df_result[(df_result.Stock == Stock) & (df_result.Market == Market)]
    try:
        df_train = df_train.loc[:,['FB_Date','y']]
        df_train['ds'] = df_train['FB_Date']
        df_train.set_index('FB_Date',inplace=True)
        df_train = df_train.loc[:,['ds','y']]
        df_train.sort_index(axis=0,ascending=True,inplace=True)
        df_train = df_train.reset_index(drop=True)
        m = Prophet()
        m.fit(df_train)
        future = m.make_future_dataframe(periods=period)
        forecast = m.predict(future)
        #print(forecast['yhat'])
        df = pd.DataFrame({'Market': Market, 'Stock': Stock, 'ds': forecast['ds'], 'yhat': forecast['yhat'] })
        return ( df )
    except: 
        print("Came to except")
        df = pd.DataFrame({'Market': Market, 'Stock': Stock, 'ds': df_train['ds'], 'yhat': 0.0 } )
        return (df)


# In[65]:

#s.groupby(level=['first', 'second']).sum()
grouped = pd.DataFrame({'count' : df_result.groupby(['Market','Stock']).size()} ).reset_index()


# In[66]:

#grouped.head()


# In[67]:

value = grouped['Stock'].count()


# In[68]:

print( str(value))


# In[69]:

#grouped = df_result.groupby(['Market','Stock'])['Day'].count()


# In[ ]:

df_output = pd.DataFrame()
i=0
for index, row in grouped.iterrows():
    i=i+1
    print("Market and Stock:"+ str(row['Market'])+"Stock:"+str(row['Stock'])+" For"+str(i) +" OF:"+str(value) )
    try:
        df_output=pd.concat([df_output,run_fb(row)])
    except:
        continue
        #df_result.merge( df_output, left_on=['Market','Stock','ds'],right_on=['Market','Stock','ds'], how='inner', indicator='_merge')


# In[53]:

#df_output


# In[ ]:

df_merge=pd.merge(left=df_result, right=df_output, left_on=['Market','Stock','ds'],right_on=['Market','Stock','ds'], how='left')


# In[ ]:

df_sub = df_merge[df_merge.Pop=='test']


# In[ ]:

#df_sub[df_sub.Stock == 363]


# In[ ]:

df_sub.to_csv("output/submission.csv")


# In[ ]:




# In[ ]:



