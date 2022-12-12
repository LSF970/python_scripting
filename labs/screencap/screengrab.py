# Import PIL, cv2 and numpy
from PIL import ImageGrab
import cv2
import numpy as np

# screen variable to capture screen, last two number in the array are the resolution
# screen = np.array(ImageGrab.grab(bbox=(0,0,800,600)))

# Show the screen as a separate window
# cv2.imshow('Python Window', screen)

# But both in a while True loop to capture the screen and show the window infinately
while True:
    screen = np.array(ImageGrab.grab(bbox=(0,0,800,600)))
    cv2.imshow('Python Window', screen)

    # This allows us to stop the loop by pressing the "q" key
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break