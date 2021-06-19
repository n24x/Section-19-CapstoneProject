import cv2
import numpy as np
import matplotlib.pyplot as plt

source_img = cv2.imread("capstone_coins.png")
img_copy = source_img.copy()
gray = cv2.cvtColor(source_img,cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(gray,(21,21),cv2.BORDER_DEFAULT)


# plt.imshow(blur_img)
# plt.show()

circles = cv2.HoughCircles(blur_img,cv2.HOUGH_GRADIENT,1,120,param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))

print(circles)

for i in circles[0,:]:
    cv2.circle(source_img,(i[0],i[1]),i[2],(0,255,0),6)
    


cv2.imshow("test" , source_img)
#cv2.waitkey()
cv2.destroyAllWindows()






























# import cv2
# import numpy as np
# import argparse
# from matplotlib import image, pyplot as plt

# img = cv2.imread("capstone_coins.png")

# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# out = gray.copy()


# #open_bgr = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# #blurred = cv2.medianBlur(open_grey,5)

# found = cv2.HoughCircles(out,cv2.HOUGH_GRADIENT,1,1000)

# if found is not None:
#     found = np.round(found[0, :]).astype("int")

#     for (x,y,r) in found:
#         cv2.found(out,(x,y),r,(0,255,0),4)
#         cv2.rectangle(out, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        
#     cv2.imshow("out", np.hstack([img, out]))
#     cv2.waitkey(0)
    
# # plt.imshow(gray)
# # plt.show()



