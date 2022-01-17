from PIL import ImageGrab
import numpy as np
import cv2

height = 500
width = 500

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
file_name = "abc.mp4"
capture_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

while True:
    screen_imgs = ImageGrab.grab(bbox = (0,0,500,500))
    array_imgs = np.array(screen_imgs)
    color_img = cv2.cvtColor(array_imgs, cv2.COLOR_BGR2RGB)
    # cv2.imshow("abc", array_imgs)
    capture_video.write(color_img)

    if cv2.waitKey(1) == ord('q'):
        break