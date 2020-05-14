# PROCESANDO CADA IMAGEN
import numpy as np
import cv2

class Image:
    """
    Permite leer, convertir a gris, dibujar rectangulo sobre la imagen, y guardar imagen
    """
    @staticmethod
    def read_image(path):
        """ Read a image from disk"""
        if isinstance(path,str):
            img = cv2.imread(path)
            return img
        else:
            print("Invalid format")
            return None
    
    @staticmethod
    def draw_over_the_image(image, x, y, width, height):
        #cv.line(image, starting cordinates, ending cordinates, color, thickness)
        #cv.rectangle(image, starting vertex, oposite vertex, color, thickness)
        #cv.circles(image, center, oposite vertex, color, thickness)
        image = cv2.rectangle(image,(x, y), (x+width, y+height),(0, 255, 0), 2)
        return image

    @staticmethod
    def convert_to_gray(image):
        # Convert image to grayscale
        print(str(image))
        img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        return img_gray   

    @staticmethod
    def save_image(path, image):
        # Write a image on disk
        # escribir validador de sstring
        name = "results/FR-result.jpg"
        cv2.imwrite(name,image)
    


