# FaceDetectionInOpenCV
Object-oriented Programming using python

** Detect faces with OpenCV in images and Video Streaming **

* OpenCV provides some pretrained classifiers stored as .xml files(haarcascades). Load clasifiers flow:
    * Load clasifier
    * Pass Image to Classifier/Detector
    * Get location/ROI for detected objects
    * Draw Rectangle over Detected Objects


## How to run
on image
python main.py --img-path /path/to/your/image

on camera video
python main.py --video 0

## There is a very insteresting example too!. It is about edges. If you want to run it, just run:
python main.py --video 1