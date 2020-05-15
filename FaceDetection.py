import cv2
import Image
import FaceDetection
from pathlib import Path
import argparse

class FaceDetection:
    """
    Utiliza haarcascade para detectar un rostro
    """
    # Returns the ROI of the detected face as a tuple
    @staticmethod
    def face_detector(img):
        face_classifier = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')
        faces = face_classifier.detectMultiScale(img,1.1,5)
        return faces

    @staticmethod
    def draw_a_rectangle_around_face(img):
        image = Image.Image
        face = FaceDetection
        gray = image.convert_to_gray(img)
        faces = face.face_detector(gray) 
        # print("Numero de caras",len(faces))
        if faces is ():
            print ("No faces found") 
        for (x, y,w,h) in faces:
            img = image.draw_rectangle_over_the_image(img,x,y,w,h)
        return img