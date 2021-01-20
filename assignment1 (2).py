#!/usr/bin/env python
# coding: utf-8

# In[6]:


lower=int(input("enter a number"))
upper=int(input("enter a number"))
print ("prime number between",lower,"and",upper,"are:")
for num in range(lower,upper):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
             print(num)
            


# In[10]:


#factorial of number
i=int(input("enter a number"))
fac=1
while i>0:
    fac=fac*i
    i=i-1
    print("factorial=",fac)


# In[11]:


#sum of n natural numbers
n=int(input("enter a number"))
i=1
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
    print("sum of first n natural numbers is",sum)


# In[ ]:





# In[ ]:




