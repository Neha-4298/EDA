#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv (r'C:\Users\Neha\Desktop\Data sets - FSDS\Pandas - 1\AgentPerformance.csv')


# In[3]:


df.head()


# In[4]:


pip install pandas-profiling


# In[5]:


from pandas_profiling import ProfileReport


# In[6]:


profile = ProfileReport(df,title='Agents Sales Data')


# In[7]:


profile


# In[ ]:




