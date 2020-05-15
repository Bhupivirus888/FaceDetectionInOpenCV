import cv2

import Image


class Edge:
    """
    Permite extraer los bordes de una imagen.
    """

    @staticmethod
    def sketch(img):
        image = Image.Image
        img = image.convert_to_gray(img)
        img_gray_blur = cv2.GaussianBlur(img,(5,5),0)
        canny_edges = cv2.Canny(img_gray_blur,10,70)
        ret, mask = cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
        return mask