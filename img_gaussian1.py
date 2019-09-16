import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Image 6.JPG')#read the image

blur = cv2.GaussianBlur(img,(5,5),0)#apply filter

plt.subplot(121),plt.imshow(img),plt.title('Original')#display the original image
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')#display the filtered image
plt.xticks([]), plt.yticks([])
plt.show()
