#!/usr/bin/env python
# coding: utf-8

# **Exploring Hacker News Posts**
# 
# Hacker News is a popular community among technology and start-up circles in which users can submit questions and posts regarding a variety of topics similar to reddit. 
# 
# This project aims to find out whether question posts or postings that show projects or general discussions reviece more comments on average and whether posts created during certain times recive more comments on average. 
# 
# 
# 
# 

# In[1]:


import csv
opened_file = open("hacker_news.csv")
hn = list(csv.reader(opened_file))
hn[:5]
          



# In[2]:


headers = hn[0]
hn=hn[1:]
print(headers)
print(hn[:4])


# In[3]:


ask_posts = []
show_posts = []
other_posts = []

for row in hn:
    title = row[1]
    if title.lower().startswith('ask hn'):
        ask_posts.append(row)
    elif title.lower().startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(row)

print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))

        
    


# In[4]:


total_ask_comments = 0
for post in ask_posts:
    total_ask_comments += int(post[4])

avg_ask_comments = total_ask_comments / len(ask_posts)
print(avg_ask_comments)


# In[5]:


total_show_comments = 0
for post in show_posts:
    total_show_comments += int(post[4])

avg_show_comments = total_show_comments/len(show_posts)
print(avg_show_comments)


# The posts with questions or ask posts recieve a greater number of responses on average. 

# In[13]:


import datetime as dt

result_list = []

for post in ask_posts:
    result_list.append(
        [post[6], int(post[4])]
    )

comments_by_hour = {}
counts_by_hour = {}
date_format = "%m/%d/%Y %H:%M"

for each_row in result_list:
    date = each_row[0]
    comment = each_row[1]
    time = dt.datetime.strptime(date, date_format).strftime("%H")
    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time] = comment
        counts_by_hour[time] = 1

comments_by_hour


# In[34]:


average_by_hour = []

for hour in comments_by_hour:
    average_by_hour.append([hour,comments_by_hour[hour]/counts_by_hour[hour]])
    
sorted(average_by_hour)    
    


# In[45]:


swap_avg_by_hour = []

for hour in average_by_hour:
    swap_avg_by_hour.append([hour[1], hour[0]])

sorted_swap = sorted(swap_avg_by_hour, reverse = True)

    
    



# In[59]:



print("Top 5 Hours for Ask Posts Comments")
for avg, hr in sorted_swap[:5]:
    print("{}: {:.2f} average comments per post".format(
            dt.datetime.strptime(hr, "%H").strftime("%H:%M"),avg
        ))
    


# In[68]:


mybday = "1989/07/27"
mybday = dt.datetime.strptime(mybday,'%Y/%m/%d')
mybday = dt.datetime.strftime(mybday,"%d-%m-%Y")

print(mybday)

