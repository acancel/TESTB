#! /usr/bin/env python
# coding: utf-8

import os
import sys
import cv2 as cv
import traceback



device = 0



capture = cv.VideoCapture(device)
print capture
for i in range(0, 10):
    ret, frame = capture.read()
cv.imwrite("image1.png", frame)