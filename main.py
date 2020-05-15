import sys
import Image
import Video
import Window
import FaceDetection
from pathlib import Path
import argparse

if __name__== '__main__':
    parser = argparse.ArgumentParser(description="Face Detection")
    parser.add_argument('--img-path', type=str, help='path to your image.')
    parser.add_argument('--video', type=str,  default=0,help='to your camera.')
    args = parser.parse_args()
    image = Image.Image
    Window = Window.Window
    if args.img_path:
        face = FaceDetection.FaceDetection
        path = args.img_path
        img = image.read_image(path)
        img = face.draw_a_rectangle_around_face(img)
        title = "Face Detection" 
        delay = 0
        Window.show_in_window(title, img, delay)
        image.save_image(img)
    else:
        Video = Video.Video
        if args.video== '0':
            detect_face = True
        else:
            # Extract edges
            detect_face = False
        Video.video_capture(detect_face)
    Window.close_window()       