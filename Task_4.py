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


t = combinations(100, 2) 


# In[4]:


p = round(1*100/t,4)


# In[5]:


print('Вероятность того, что 2 приобретенных билета окажутся выигрышными =', p, '%')

