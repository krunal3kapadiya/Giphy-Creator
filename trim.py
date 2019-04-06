#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:30:25 2019
Desription: trimming video
@author: krunal
"""
import argparse
import os
import re
import cv2
import imageio

AP = argparse.ArgumentParser()
AP.add_argument("--starttime", required=True, help="Start time")
AP.add_argument("--endtime", required=True, help="End time")
AP.add_argument("--video", required=True, help="Video path")
AP.add_argument("--outputfilename", required=True, help="Output file name")
AP.add_argument("--filetype", required=True, help="GIPHY or MP4")
ARGS = vars(AP.parse_args())

#check the length of the video
video_path = ARGS['video']
output_file_name = ARGS['outputfilename']
giphy_or_mp4 = ARGS['filetype']
starttime = ARGS['starttime']
endtime = ARGS['endtime']

starttime = int(starttime.split(':')[0]) * 60 + int(starttime.split(':')[1])
endtime = int(endtime.split(':')[0]) * 60 + int(endtime.split(':')[1])

videoCap = cv2.VideoCapture(video_path)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
length = int(videoCap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(videoCap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(videoCap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = videoCap.get(cv2.CAP_PROP_FPS)

################ reading and appendding frames array
success, image = videoCap.read()
img = []
while success:
    img.append(image)
    success, image = videoCap.read()

################ taking fps and frames time to cut
startframe = int(fps) * starttime
endframe = int(fps) * endtime

############## if giph then only save giph or else MP4
if re.match(giphy_or_mp4, 'GIPHY'):
    gif_images = []
    #    img[j] = cv2.cvtColor(img[j], cv2.COLOR_BGR2GRAY)
    gif_images.extend([img[j] for j in range(startframe, endframe)])
    imageio.mimsave(os.path.join(output_file_name+'.gif'), gif_images, duration=1/25)
    print('GIF Saved successfully')
elif re.match(giphy_or_mp4, 'MP4'):
    out = cv2.VideoWriter(output_file_name+'.mp4', fourcc, 20.0, (640, 480))
    for j in range(startframe, endframe):
        out.write(img[j])
    out.release()
    print('Video Saved successfully')
else:
    print('Please select valid file type')
