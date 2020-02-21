#!/usr/bin/env python
# coding: utf-8

# In[1]:


from itertools import permutations


# In[2]:


p = permutations('0123456789')


# In[3]:


solution = 0


# In[4]:


for i in p:
    if (int(''.join(i[7:10])) % 17 == 0 and
        int(''.join(i[6:9])) % 13 == 0 and
        int(''.join(i[5:8])) % 11 == 0 and
        int(''.join(i[4:7])) % 7 == 0 and
        int(''.join(i[3:6])) % 5 == 0 and
        int(''.join(i[2:5])) % 3 == 0 and
        int(''.join(i[1:4])) % 2 == 0):
        solution += int(''.join(i))


# In[5]:


print (solution)

