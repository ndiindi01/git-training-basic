#!/usr/bin/env python
# coding: utf-8

# In[1]:


##20##


# In[2]:


from math import factorial
fact100 = factorial(100)
strfact=list(str(fact100))
strfact = [int(x) for x in strfact]
sum_of_the_digits = sum(strfact)
print("100!=",fact100)
print ("sum of the digits in the number 100!=",sum_of_the_digits)

