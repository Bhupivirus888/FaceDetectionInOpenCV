import cv2
import FaceDetection
import Window
import Edge

class Video:
    """
    Permite Activar la video camara y capturar cada imagen para detectar rostros dentro de la imagen.
    """

    @staticmethod
    def video_capture(face_detect = True):
        window = Window.Window
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            if face_detect:
                face = FaceDetection.FaceDetection
                img = face.draw_a_rectangle_around_face(img)
            else:
                edge = Edge.Edge
                img = edge.sketch(img)
            title = "Camera video active"
            delay = 13
            continue_showing = window.show_in_window(title, img, delay)
            if not continue_showing:
                break
        cap.release()