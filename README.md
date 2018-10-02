This is a Project of Innovation Workshop 2018 at Skoltech.

This project devoted to finding lost people (in a fields, swamps, mountains) by camera attached to a drone, so computer vision is used (darknet). Onboard processing perfomed by Raspberry Pi, but neural network works on external server.

There are server code and raspeberry code. Assumed that server code located at ~/darknet/.

In order to run this on raspberry use:
```
python record.py
```

After that recording is performed and image is sent to server.

In order to process image on server you need to download weights in a server folder by
```
wget https://pjreddie.com/media/files/yolo.weights
```
