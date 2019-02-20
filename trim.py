#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:30:25 2019
Desription: trimming video
@author: krunal
"""
import argparse
import cv2
AP = argparse.ArgumentParser()
AP.add_argument("-i", "--video", required=True, help="Video path")
ARGS = vars(AP.parse_args())

videoCap = cv2.VideoCapture('big_buck_bunny.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

success, image = videoCap.read()
length = int(videoCap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(videoCap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = videoCap.get(cv2.CAP_PROP_FPS)
count = 0
img = []
while success:
    img.append(image)
    success, image = videoCap.read()
    count += 1
video = cv2.VideoWriter('newVideo.mp4', -1, 1, (width, height))
for j in range(0, 5):
    video.write(img[j])
    out.write(img[j])
cv2.destroyAllWindows()
out.release()
video.release()
