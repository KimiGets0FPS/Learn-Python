import numpy as np
from PIL import ImageGrab
import cv2
from on_click import OnClick
# import time


class SeeScreen:
    # def reeeeee(self):
    # last_time = time.time()
    image = ImageGrab.grab()
    while True:
        print_screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
            # print('loop took {} seconds'.format(time.time()-last_time))
            # last_time = time.time()
        cv2.imshow("Let's Go AimBot", cv2.cvtColor(print_screen, cv2.COLOR_BGR2RGB))
        #* Checking if there is red on the team.
        for y in range(0, 100, 10):
            for x in range(0, 100, 10):
                color = image.getpixel((x, y))
            # print(time.clock())
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


# SeeScreen
