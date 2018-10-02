#!/bin/bash

scp data/pict.jpg server:~/darknet
ssh server 'bash ~/darknet/detect.sh'
