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
import os

def check_person(img):
    return detectPeople(img)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max_frame', type=int, default=10)
    parser.add_argument('--time_lag', type=float, default=0)
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
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imwrite(path+'pict.jpg'.format(frame), img)
        print('Frame {}'.format(frame))
        os.system('sh send.sh')
#        if check_person(img):
#            print('Person detected!')
#            os.system('sh send.sh')
            #camera.start_recording(os.path.join(path, 'video.h264'))
            #time.sleep(args.video_duration)
            #camera.stop_recording()
        time.sleep(args.time_lag)

