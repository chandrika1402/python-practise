#!/usr/bin/env python
# coding: utf-8

# In[1]:


month1_set = {"Jan","Feb","Dec","Mar"}
month2_set = {"May","Jan","Oct","Mar"}


# In[2]:


month1_set


# In[3]:


month2_set


# In[5]:


month=month1_set | month2_set                       #Concadination of two sets
month


# In[6]:


month_common=month1_set.union(month2_set)              #Concadination of two sets
month_common


# In[7]:


common = month1_set & month2_set                    #union of two sets
common


# In[8]:


month_common = month1_set.intersection(month2_set)          #union of two sets
month_common


# In[10]:


diff = (month1_set - month2_set)                           #Differece between the sets
diff


# In[11]:


x=month1_set.difference(month2_set)                       #Differece between the sets
x


# In[ ]:




