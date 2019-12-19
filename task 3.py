#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


nltk.download()


# In[3]:


from nltk.corpus import brown


# In[4]:


brown.categories()


# In[5]:


brown.words(categories='adventure')


# In[6]:


brown.words(categories='adventure')[:100]


# In[7]:


from nltk.corpus import inaugural


# In[8]:


inaugural.fileids()


# In[9]:


inaugural.words(fileids='1861-Lincoln.txt')


# In[10]:


inaugural.words(fileids='2009-Obama.txt')


# In[11]:


from nltk.corpus import book


# In[12]:


from nltk.book import *


# In[13]:


f=FreqDist(text1)


# In[14]:


f.most_common(10)


# In[15]:


g=FreqDist(1977-Carter.txt)


# In[16]:


g=FreqDist('1977-Carter.txt')


# In[17]:


g.most_common(10)


# In[ ]:




