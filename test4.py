#! /usr/bin/env python
# coding: utf-8

import os
import sys
#import traceback
import cv2
import numpy as np
from matplotlib import pyplot as plt
#from qrtools import QR

#if __name__ == "__main__":
#    device = 0
#    decode = True
capture = cv2.VideoCapture(0)
for i in range(0, 10):
    ret, frame = capture.read()
cv2.imwrite("image.jpg", frame)


img = cv2.imread('image.jpg',0)
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

