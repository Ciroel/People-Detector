#!/bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
./darknet detect cfg/yolov2.cfg yolo.weights pict.jpg > result.txt
number=$(cat result.txt | grep person | wc -l)
echo $number
if (($number>0))
then
    echo 'People detected!'
    sh bot.sh
else
    echo 'No people'
fi

