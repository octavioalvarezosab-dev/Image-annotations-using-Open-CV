import cv2
import numpy as np

# Global variables
annotations = []
current_annotation = []

# Mouse callback function
def draw_circle(event, x, y, flags, param):
    global current_annotation
    if event == cv2.EVENT_LBUTTONDOWN:
        current_annotation = [(x, y)]
    elif event == cv2.EVENT_MOUSEMOVE:
        if current_annotation:
            current_annotation[0] = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        if current_annotation:
            annotations.append(current_annotation[0])
            current_annotation = []

# Load an image
image = np.zeros((600, 800, 3), dtype=np.uint8)  # Black image for annotation
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_circle)

while True:
    # Create a copy of the image to draw annotations
    img_copy = image.copy()
    for annotation in annotations:
        cv2.circle(img_copy, annotation, 5, (0, 255, 0), -1)  # Draw green circle
    if current_annotation:
        cv2.circle(img_copy, current_annotation[0], 5, (0, 0, 255), -1)  # Draw red circle for current annotation

    cv2.imshow('Image', img_copy)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key
        break

cv2.destroyAllWindows()