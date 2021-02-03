#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import stock_data
stock_data_df=pd.read_csv("stock_data/AMC.csv")
display(stock_data_df)


# In[22]:


stock_data_df.set_index("Date",inplace = True)
stock_data_df['Close'].plot()
stock_data_df.head()


# In[27]:


reddit_data_df=pd.read_csv("reddit_cleaned/organized_reddit_data.csv")
display(reddit_data_df)


# In[24]:


df['AMC'].plot()


# In[ ]:




