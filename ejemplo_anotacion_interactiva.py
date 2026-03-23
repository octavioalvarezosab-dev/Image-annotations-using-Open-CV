import cv2
import numpy as np

# Global variables
drawing = False # true if mouse is pressed
ix, iy = -1, -1

# Mouse callback function

def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)

# Create a black image, a window, and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27: # press 'ESC' to exit
        break
cv2.destroyAllWindows()