#!/usr/bin/env python
# coding: utf-8

# In[3]:


import nltk
from nltk.stem import PorterStemmer
stemmerporter=PorterStemmer()
stemmerporter.stem('happiness')


# In[4]:


import nltk
from nltk.stem import PorterStemmer
stemmerporter=PorterStemmer()
stemmerporter.stem('happiness')


# In[5]:


import nltk
from nltk.stem import PorterStemmer
stemmerporter=PorterStemmer()
stemmerporter.stem('lying')


# In[6]:


import nltk
from nltk.stem import RegexStemmer
stemmerregexp=RegexpStemmer('ing')
stemmerregexp.stem('sing')


# In[7]:


import nltk
from nltk.stem import LancasterStemmer
lancasterporter=LancasterStemmer()
lancasterporter.stem('happiness')


# In[8]:


import nltk
from nltk.stem import SnowballStemmer
SnowballStemmer.languages
frenchstemmer=SnowballStemmer('french')
snowballstemmer.stem('manges')


# In[9]:


#LEMMATIZATION
from nltk.stem import WordLemmatizer
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("cacti"))


# In[10]:


import nltk
from nltk.stem import RegexpStemmer
stemmerregexp=RegexpStemmer('ing')
stemmerregexp.stem('sing')


# In[12]:


from nltk.stem import WordNetLemmatizer


# 

# 

# In[14]:


lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("cacti"))


# In[15]:


lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("Am"))


# In[16]:


from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
example="Am quick brown fox jumps over a lazy dog"
example=[stemmer.stem(token) for token in example.split(" ")]
print(" ".join(example))


# In[17]:


import nltk
from nltk.stem import SnowballStemmer
SnowballStemmer.languages


# In[18]:


snowballstemmer=SnowballStemmer('english')
snowballstemmer.stem('understandable')


# In[ ]:




