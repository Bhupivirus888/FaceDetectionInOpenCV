import sys
import cv2
import numpy as np
import Image
from pathlib import Path
import argparse

def face_detector(imagen):
    # Returns the ROI of the detected face as a tuple
    # It stores the top left coordinate and the bottom right coordiantes.
    face_classifier = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')
    # Image, scaleFactor and minNeighbours
    faces = face_classifier.detectMultiScale(imagen,1.1,5)
    return faces

def draw_a_rectangle_over_image(image):
    gray = Image.convert_to_gray(image)
    faces = face_detector(gray) 
    # print("Numero de caras",len(faces))
    if faces is ():
        print ("No faces found") 
    for (x, y,w,h) in faces:
        image = Image.draw_over_the_image(image,x,y,w,h)
    cv2.imshow('Face Detection', image)
    return image

def sketch(image):
    img = Image.convert_to_gray(image)
    # Clean up image using Gaussian Blur
    img_gray_blur = cv2.GaussianBlur(img,(5,5),0)
    # Extract edges
    canny_edges = cv2.Canny(img_gray_blur,10,70)
    # Binary Image (black and white)
    ret, mask = cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
    return mask

if __name__== '__main__':
    parser = argparse.ArgumentParser(description="Face Detection")
    parser.add_argument('--img-path', type=str, help='path to your image.')
    parser.add_argument('--video', type=str,  default=0,help='to your camera.')
    args = parser.parse_args()
    Image = Image.Image
    if args.img_path:
        path = args.img_path
        image = Image.read_image(path)
        image = draw_a_rectangle_over_image(image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        Image.save_image("",image)
    else:
        if args.video== '0':
            cap = cv2.VideoCapture(0)
            while True:
                # Read the frame
                ret, img = cap.read()
                img = draw_a_rectangle_over_image(img)
                # Stop if enter key is pressed
                if cv2.waitKey(1) ==13:  # 13 is the Enter key
                    break
            cap.release()
        else:
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                cv2.imshow('Live Sketcher', sketch(frame))
                if cv2.waitKey(1) ==13:  
                    break
            cap.release()
    cv2.destroyAllWindows()            