#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from scipy.stats import  binom
from scipy.stats import  poisson


# In[2]:


def combinations(n, k):
    return (np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)))


# In[3]:


# Из колоды в 52 карты извлекаются случайным образом 4 карты.


# In[4]:


# a) Найти вероятность того, что все карты – крести


# In[5]:


a = combinations(13, 4)


# In[6]:


t = combinations(52, 4)


# In[7]:


p = round(a*100/t,2)


# In[8]:


print('Вероятность того, что все карты – крести =',p, '%')


# In[9]:


#б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.


# In[10]:


# Найти все комбинации для тузов (1-й вариант решения)


# In[11]:


a1=combinations(4, 1)


# In[12]:


a2=combinations(4, 2)


# In[13]:


a3=combinations(4, 3)


# In[14]:


a4=combinations(4, 4)


# In[15]:


b1=combinations(48,3)


# In[16]:


b2=combinations(48,2)


# In[17]:


b3=combinations(48,1)


# In[18]:


p=round((a1*b1+a2*b2+a3*b3+a4)*100/t,2)


# In[19]:


print('Вероятность того, что среди 4-х карт окажется хотя бы один туз =',p, '%')


# In[20]:


# Найти все комбинации без тузов (2-й вариант решения)


# In[21]:


a=combinations(48,4)


# In[22]:


p=round((1-a/t)*100,2)


# In[23]:


print('Вероятность того, что среди 4-х карт окажется хотя бы один туз =',p, '%')

