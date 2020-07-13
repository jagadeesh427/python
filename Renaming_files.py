#!/usr/bin/env python
# coding: utf-8

# In[25]:


#renaming the video file names in a folder
import os

os.chdir('/Users/jagadeeshyadav/Desktop/python/parse')
print(os.getcwd())

for f in os.listdir():
   #print(f)
   f_name, f_ext = os.path.splitext(f)
   f_title, f_course, f_num = f_name.split('-')
   f_title = f_title.strip()
   f_course = f_course.strip()
   f_num = f_num.strip()[1:].zfill(2)
   new_name = '{}-{}{}'.format(f_num, f_title,f_ext)
   os.rename(f,new_name)

