# Python ScreenCapture

## Timings

30 minutes

## Summary

A simple way to capture your screen using Python scripts

## Guide

First import the libraries PIL (image processing) and cv2 (capture)

```
from PIL import ImageGrab
import cv2
```

Lets use the ImageGrab method from PIL.
Create a variable called screen, and in it have an ImageGrab.grab object as an array:

```
screen = np.array(ImageGrab.grab(bbox=(0,0,800,600)))
```

cv2 hass a function called imshow(). This allows us to show the screen in a window. Lets call it 'Python Window' in our script:

```
cv2.imshow('Python Window', screen)
```

Now we want to put both of these inside a loop so that the screen is continuously grabbed and the window is continnuously showed. We want an infinate loop here, so While True useful:

```
while True:
    screen = np.array(ImageGrab.grab(bbox=(0,0,800,600)))
    cv2.imshow('window', screen)
```

Finally, we need a way to exit this infinate loop when we want. Pressing the "q" key seems to be popular for  Python programs, so lets use that:

```
if cv2.waitKey(25) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    break
```

Full code:

```
from PIL import ImageGrab
import cv2
import numpy as np

while True:
    screen = np.array(ImageGrab.grab(bbox=(0,0,800,600)))
    cv2.imshow('Python Window', screen)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
```