import cv2

class Image:
    """
    Permite leer, convertir a gris, dibujar rectangulo sobre la imagen, y guardar imagen
    """

    # Read a image from disk
    @staticmethod
    def read_image(path):
        if isinstance(path,str):
            img = cv2.imread(path)
            return img
        else:
            print("Invalid format")
            return None
    
    @staticmethod
    def draw_rectangle_over_the_image(image, x, y, width, height):
        image = cv2.rectangle(image,(x, y), (x+width, y+height),(0, 255, 0), 2)
        return image

    @staticmethod
    def convert_to_gray(image):
        print(str(image))
        img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        return img_gray   

    @staticmethod
    def save_image(image):
        name = "results/FR-result.jpg"
        cv2.imwrite(name,image)
    


