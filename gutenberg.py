#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib import request


# In[2]:


url="http://www.gutenberg.org/files/2554/2554-0.txt"


# In[3]:


response=request.urlopen(url)


# In[4]:


raw=response.read().decode('utf8')


# In[5]:


type(raw)


# In[6]:


len(raw)


# In[7]:


raw[:75]


# In[8]:


from nltk.tokenize import word_tokenize


# In[9]:


tokens=word_tokenize(raw)


# In[10]:


type(tokens)


# In[11]:


len(tokens)


# In[12]:


tokens[:10]


# In[ ]:




