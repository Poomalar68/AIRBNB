# Airbnb-booking-Analysis-EDA- 
I chose this project to understand the trends of Airbnb in New York City area and analysis is done through addressing the following questions:

 What can we learn about different hosts and areas?
 
 What can we learn from predictions? (ex: locations, prices, reviews, etc)
 
 Which hosts are the busiest and why?
 
 Is there any noticeable difference of traffic among different areas and what could be the reason for it? 
 
 Which is the expensive location in dataset?
 
 What are the different room types available?
 
 How room types are distributed at different locations?
 
 
 **Data Preparation**
 
This dataset has more than 49000 observations and 13 features. The target features for analysis are   host_id, Neighbourhood_group,neighbourhood, room_type, price,number_of_reviews. To proceed with the analysis, data wrangling should be done as this data set is really messy.
I had to clean up the values in several columns: number_of_reviews.
The data types for other columns like property_name, host_name,last_review etc.are not necessary for analysis so I dropped them.


**Result**

This Airbnb dataset for year 2019 appeared to be very rich dataset with variety of features that allowed me to do deep data exploration on each significant column present .Firstly I have found top 10 listing areas, then I found top host who take good advantage of Airbnb platform and provide most listings, top host has 327 listings .I also found that out of 221 areas Williamsburg is topmost area with total 3920 listings. I also found that out of five locations Manhattan includes 44.3% of listings within it also I found that Manhattan is most expensive location in New York city. Using features like latitude, longitude, neighbourhood_group, I found distribution of listings in different location. Using different features I found major reasons for traffic among different areas, room types available in different areas. Overall I discovered good number of interesting relationships between features and visualise them. This data analytics is very useful on higher level on Airbnb machine learning team for better business decision, control over platform, marketing initiatives, and implementation of new features.
