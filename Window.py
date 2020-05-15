import cv2

class Window:
    """
    Permite abrir y cerrar ventanas para desplegar imagenes.
    """
    @staticmethod
    def show_in_window(name, image, delay = 0):
        cv2.imshow(name,image)
        show = cv2.waitKey(delay)
        go_on = True
        if  show == 13:
            go_on = False
        return go_on


    @staticmethod
    def close_window():
        cv2.destroyAllWindows() 
    
