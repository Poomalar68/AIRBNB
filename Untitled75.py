#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly 
import missingno as msno
import plotly.graph_objects as go
from sklearn import datasets


# In[ ]:


airbnb =pd.read_csv('ab_nyc_2019.csv')
airbnb.head()


# In[ ]:


airbnb.tail()


# In[ ]:


airbnb.shape


# In[ ]:


airbnb.info()


# In[ ]:


airbnb.columns


# In[ ]:


airbnb.describe()


# In[ ]:


airbnb.drop(['id','name','host_name','last_review'],axis=1,inplace =True)
airbnb.head()


# In[ ]:


airbnb.isnull().sum()


# In[ ]:


msno.matrix(airbnb)


# In[ ]:


airbnb['reviews_per_month'].fillna(0,inplace=True)
airbnb


# In[ ]:


airbnb.isnull().any()


# In[ ]:


msno.matrix(airbnb)


# In[ ]:


airbnb.shape


# In[ ]:


airbnb.neighbourhood.unique()


# In[ ]:


len(airbnb.neighbourhood.unique())


# In[ ]:


Number_of_hosts=airbnb.host_id.unique()
Number_of_hosts


# In[ ]:


len(Number_of_hosts)


# In[ ]:


top_host_id = airbnb['host_id'].value_counts().head(10)
top_host_id


# In[ ]:


top_host_id.sum()


# In[ ]:


top_host_id.plot(kind='bar')
plt.title=('top_10 host_id')
plt.ylabel=('count')
plt.xlabel=('host_id')


# In[ ]:


# Let us see correletion between the predictions such as location, price, reviews
corr=airbnb.corr(method='Brooklyn')
plt.figure(figsize=(13,10))
plt.title=('correlation between location, price,reviews\n')
sns.heatmap(corr,annot=True)
plt.show()


# In[ ]:


airbnb.neighbourhood_group.unique()


# In[ ]:


location =airbnb['neighbourhood_group'].value_counts()
location


# In[ ]:


len(location)


# In[ ]:


#Visualise number of listings  in different locations with help of pie chart.
plt.style.use('fivethirtyeight')
plt.figure(figsize=(13,7))
plt.title=("neighbourhood group")
g=plt.pie(airbnb.neighbourhood_group.value_counts(),labels=airbnb.neighbourhood_group.value_counts().index,autopct='%1.1f%%',startangle=180)
plt.show()


# In[ ]:


price_vs_location =airbnb.groupby(['neighbourhood_group'])['price'].mean()
price_vs_location


# In[ ]:


# Let us visualise price_vs_location .
ax= price_vs_location.plot.bar(figsize=(10,5),fontsize=14)
ax.set_title('price per different location',fontsize=20)
ax.set_xlabel('neighbourhood',fontsize=15)
ax.set_ylabel('price',fontsize=15)


# In[ ]:


most_reviewed_listings=airbnb.nlargest(10,'number_of_reviews')
most_reviewed_listings


# In[ ]:


reviewed_per_listings= airbnb.filter(['neighbourhood_group','number_of_reviews'])
reviewed_per_listings


# In[ ]:


top_reviewed_listings=reviewed_per_listings.nlargest(10,'number_of_reviews')
top_reviewed_listings


# In[ ]:


# Let us find the busiest host using host_id and minimum nights column in our dataset.
Busy_host=airbnb.groupby(['host_id']).minimum_nights.mean()
Busy_host=Busy_host.sort_values(ascending=True)
Busy_host


# In[ ]:


# Let us find top 10 busy hosts.
Top_busy_hosts=Busy_host.tail(10)
Top_busy_hosts


# In[ ]:


# Let us visualise top 10 busy hosts to find busiest host using bar plot.
plt.rcParams['figure.figsize']=(10,5)
Top_busy_hosts.plot(kind='bar')
plt.title=('Top_busy_host')
plt.ylabel=('minimum_nights')
plt.xlabel=('host_id')
plt.show


# In[ ]:


plt.figure(figsize=(10,6))
sns.scatterplot(airbnb.longitude,airbnb.latitude,hue=airbnb.neighbourhood_group)
plt.ioff


# In[ ]:


top_listing_area = airbnb['neighbourhood'].value_counts().head(20)
top_listing_area


# In[ ]:


price_of_listing=airbnb.groupby(['neighbourhood']).price.mean()
price_of_listing=price_of_listing.sort_values(ascending=True)
price_of_listing


# In[ ]:


# Let us check wheather availability over year have any effect on number of listings in perticular area.
availability_in_year=airbnb.groupby(['neighbourhood']).availability_365.sum()
availability_in_year=availability_in_year.sort_values(ascending=False)
availability_in_year


# In[ ]:


maximum_reviews=airbnb.groupby(['neighbourhood']).number_of_reviews.sum()
maximum_reviews=maximum_reviews.sort_values(ascending=False)
maximum_reviews


# In[ ]:


most_expensive_area=airbnb.groupby(['neighbourhood_group']).price.mean()
most_expensive_area=most_expensive_area.sort_values(ascending=False)
most_expensive_area


# In[ ]:


# Let us visualise most_expensive_area using bar plot
most_expensive_area.plot(kind='bar')
plt.title=('most_expensive_area')
plt.xlable=('neighbourhood_group')
plt.ylable=('price')


# In[ ]:


room_type=airbnb.groupby(['room_type']).room_type.count()
room_type=room_type.sort_values(ascending=False)
room_type


# In[ ]:


plt.figure(figsize=(10,7))
plt.title=("Type of rooms")
sns.countplot(airbnb.room_type, palette='muted')
fig = plt.gcf()
plt.show()


# In[ ]:


# Let us visualise room_type location per neighbourhood group
sns.set(rc={'figure.figsize':(10,10)})
title='Room types location per neighbourhood group'
sns.catplot(x='room_type',kind='count',hue='neighbourhood_group',data=airbnb);
plt.title=(title)
plt.ioff()


# In[ ]:


# Let us visualise relationship  between neighbourhood group and availability 365 using boxplot
plt.figure (figsize= (10,10))
ax= sns.boxplot(data=airbnb,x='neighbourhood_group',y='availability_365',palette='plasma')


# In[ ]:




