#!/bin/bash

scp data/pict.jpg server:~/darknet
ssh server '¬/darknet/detect.sh'
