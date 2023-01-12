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


t = combinations(15, 3)


# In[4]:


a = combinations(9, 3)


# In[5]:


p = round(100*a/t,2)


# In[6]:


print('Вероятность того, что все извлеченные детали окрашены =',p, '%')

