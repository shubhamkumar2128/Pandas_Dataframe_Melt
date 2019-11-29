#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
df=pd.read_csv("C:\\csvdemo.csv")
print(df)


# In[145]:


df2=pd.melt(df,id_vars=["day"])
print(df2)


# In[153]:


#Filter specific
df2=pd.melt(df,id_vars=["day"],var_name="city")
df2=df2[df2["city"]=="lucknow"]
print(df2)


# In[149]:


df2=pd.melt(df,id_vars=["day"],var_name="city",value_name="temperature")
print(df2)


# In[ ]:




