#!/usr/bin/env python
# coding: utf-8

# In[1123]:


import cv2
import numpy as np
import matplotlib.pyplot as plt

source_img = cv2.imread("capstone_coins.png")
img_copy = source_img.copy()
gray = cv2.cvtColor(source_img,cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(gray,(21,21),cv2.BORDER_DEFAULT)

# plt.imshow(gray)
# plt.show()


# In[1124]:


blur_img = cv2.GaussianBlur(gray,(21,21),cv2.BORDER_DEFAULT)

# plt.imshow(blur_img)
# plt.show()


# In[1125]:


scale_percent = 30 # percent of original size
width = int(blur_img.shape[1] * scale_percent / 100)
height = int(blur_img.shape[0] * scale_percent / 100)
dim = (width, height)

blur_img = cv2.resize(blur_img, dim, interpolation = cv2.INTER_AREA)

# plt.imshow(blur_img)
# plt.show()


# In[1126]:


circles = cv2.HoughCircles(blur_img,cv2.HOUGH_GRADIENT,1.2,40,param1=50,param2=35,minRadius=20,maxRadius=60)
circles = np.uint16(np.around(circles))


# In[1127]:


#circles = cv2.HoughCircles(blur_img,cv2.HOUGH_GRADIENT,1.2,60,param1=50,param2=35,minRadius=20,maxRadius=60) circles = np.uint16(np.around(circles))


# In[1128]:


for i in circles[0,:]:
    cv2.circle(blur_img,(i[0],i[1]),i[2],(0,200,0),1)
    cv2.circle(blur_img,(i[0],i[1]),2,(0,0,255),1)
    
plt.rcParams['figure.figsize'] = [16,9]
plt.imshow(blur_img)


# In[1129]:


print(circles)
print("Found  " + str(circles.shape[1]) + " so far" )


# In[ ]:





# In[1130]:


#print(circles[0])
      


# In[ ]:





# In[1131]:


q,p,t = 0,0,0
for i in range(circles.shape[1]):
    if (circles[0][i][j+2]) > 38:
        q += 1
#         print("we have a quoter")
    elif (circles[0][i][j+2]) < 37 and (circles[0][i][j+2]) > 30:
        p +=1
#         print("we have a penny")
    elif (circles[0][i][j]) > 25:
        t +=1
#         print("we have a 10 cent")
        
print(f"we have {q} quoters and {t} ten cents and {p} penny's ")


# In[ ]:




