#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.corpus import stopwords
stopwords.words("english")


# In[2]:


import nltk
entries=nltk.corpus.cmudict.entries()
len(entries)


# In[3]:


for entry in entries[10000:10025]
print(entry)


# In[4]:


for entry in entries[10000:10025]:
print(entry)


# In[5]:


for entry in entries[10000:10025]
    print(entry)


# In[6]:


for entry in entries[10000:10025]:
    print(entry)


# In[7]:


from nltk.corpus import wordnet as wn
wn.synsets('motorcar')


# In[8]:


wn.synswt('car.n.01').lemma_names()


# In[9]:


wn.synset('car.n.01').lemma_names()


# In[10]:


import nltk
texts=["""Wondering if I should quit work and become a monk who secretly writes serial nurder thriller novels.
Going to bed.
gary coleman sighting by Zoom. The rumors were true
Festmob."""]


# In[1]:


from text in texts:
    sentences=nltk.sent_tokenize(text)
    for sentence in sentences:
        words=nltk.word_tokenize(sentence)
        tagged_words=nltk.pos_tag(words)
        print(tagged_words)


# In[2]:


import nltk
texts=["""Wondering if I should quit work and become a monk who secretly writes serial nurder thriller novels.
Going to bed.
gary coleman sighting by Zoom. The rumors were true
Festmob."""]


# In[3]:


from text in texts:
    sentences=nltk.sent_tokenize(text)
    for sentence in sentences:
        words=nltk.word_tokenize(sentence)
        tagged_words=nltk.pos_tag(words)
        print(tagged_words)


# In[4]:


for text in texts:
    sentences=nltk.sent_tokenize(text)
    for sentence in sentences:
        words=nltk.word_tokenize(sentence)
        tagged_words=nltk.pos_tag(words)
        print(tagged_words)


# In[5]:


import nltk
from nltk.tokenize import TweetTokenizer
text=' in support of :) #worldwar3'
twtkn=TweetTokenizer()
twtkn.tokenize(text)


# In[6]:


from nltk.corpus import brown
news_text=brown.words(categories='news')
fdist=nltk.FreqDist(w.lower() for w in news_text)
modals=['can','could','may','might','must','will']
for m in modals:
    print(m)


# In[ ]:




