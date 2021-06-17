import cv2
from matplotlib import pyplot as plt

img = cv2.imread("capstone_coins.png")

open_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
open_bgr = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
blurred = cv2.medianBlur(open_grey,5)

found = cv2.HoughCircles(
                         blurred,
                         cv2.HOUGH_GRADIENT,
                         1,
                         40,
                         param1=50,
                         param2=30,
                         minRadius=50,
                         maxRadius=30,
                         )

plt.imshow(blurred)
plt.show()



