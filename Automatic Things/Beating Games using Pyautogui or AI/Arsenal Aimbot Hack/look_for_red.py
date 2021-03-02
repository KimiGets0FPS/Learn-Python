import numpy as np
from PIL import ImageGrab
import cv2
# import time


RED = 234, 67, 53
image = ImageGrab.grab()
while True:
    # start_time = time.time()
    print_screen = np.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080)))
    cv2.imshow("Aimbot Screen", cv2.cvtColor(print_screen, cv2.COLOR_BGR2RGB))
    # print(f"Time to update: {time.time()-start_time}")
    # Checking if there is red on the team.
    for y in range(0, 100, 10):
        for x in range(0, 100, 10):
            if image.getpixel((x, y)) == RED:
                break
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
