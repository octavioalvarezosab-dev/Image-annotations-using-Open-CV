# Basic Image Annotation Examples in OpenCV

import cv2
import numpy as np

# Load an image
image = cv2.imread('image.jpg')

# Draw a rectangle
cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), 2)

# Draw a circle
cv2.circle(image, (300, 300), 50, (0, 255, 0), -1)

# Put text on the image
cv2.putText(image, 'OpenCV Annotation', (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Show the image
cv2.imshow('Annotated Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()