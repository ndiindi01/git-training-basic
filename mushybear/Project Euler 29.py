#!/usr/bin/env python
# coding: utf-8

# In[1]:


##29##


# In[2]:


powers = []
for a in range(2,101):
        for b in range(2,101):
                powers.append(a**b)
powers = set(powers)
print ("distinct terms:",len(powers))

