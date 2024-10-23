
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from os import path


print("Enter the image name (in the same dir as this script): ")
imageName = input()
if not path.exists(imageName):
    print("Image Not Found!")
    exit()

img = cv.imread("image.jpg")
b, g, r = cv.split(img)
cv.imshow("img", img)
# cv.imshow("b", b)
# cv.imshow("g", g)
# cv.imshow("r", r)
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()
cv.waitKey(0)