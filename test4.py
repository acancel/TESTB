#! /usr/bin/env python
# coding: utf-8

import os
import sys
#import traceback
import cv2 as cv
#from qrtools import QR

#if __name__ == "__main__":
#    device = 0
#    decode = True
capture = cv.VideoCapture(0)
for i in range(0, 10):
    ret, frame = capture.read()
cv.imwrite("image.jpg", frame)
    