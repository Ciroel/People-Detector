import picamera
import picamera.array
import time
import os
import argparse
import cv2
import warnings
import numpy as np
from detect import detectPeople
warnings.filterwarnings('ignore')

def check_person(img):
    return detectPeople(img)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max_frame', type=int, default=10)
    parser.add_argument('--time_lag', type=float, default=1)
    parser.add_argument('--video_duration', type=float, default=5)
    return parser.parse_args()

if __name__=='__main__':
    args = parse_args()
    camera = picamera.PiCamera()
    path = './data/'
    for frame in range(1, args.max_frame):
        img = picamera.array.PiRGBArray(camera)
        camera.start_preview()
        camera.capture(img, 'rgb')
        img = img.array
        cv2.imwrite(path+'pict_{}.jpg'.format(frame), img)
        print('Frame {}'.format(frame))
        if check_person(img):
            print('Person detected!')
            camera.start_recording(os.path.join(path, 'video.h264'))
            time.sleep(args.video_duration)
            camera.stop_recording()
        time.sleep(args.time_lag)

