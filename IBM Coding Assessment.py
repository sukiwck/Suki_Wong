#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1

No_of_Tshirts = input('The total number of T-shirts: ')
Tshirts = input('T-shirts sizes: ')
No_of_Requests = input('The total number of requests: ')
requested_sizes = input('Request sizes: ')

fulfilled = True

if requested_sizes in Tshirts:
    fulfilled = True
else:
    fulfilled = False

print(fulfilled)


# In[ ]:


#Q2

allValid = True
errorCodes = []
for each record in input file:
    allValid = record.isValid
    if record.isValid is not true:
        errorCodes.append('error message')
if allValid is True:
    print("Yes")
else:
    print("No")
    print(errorCodes)


# In[ ]:


#Q3

SELECT owner_id, owner_name, COUNT(DISTINCT(category_id)) FROM owner
INNER JOIN article ON owner.owner_id = article.owner_id
INNER JOIN category_article_mapping ON article.article_id = category_article_mapping.article_id
SORT BY COUNT(DISTINCT(category_id))

