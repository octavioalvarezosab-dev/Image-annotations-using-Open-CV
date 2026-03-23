import cv2
import numpy as np

# Load an image
image = cv2.imread('image.jpg')

# Draw a rectangle
start_point = (50, 50)  # (x, y)
end_point = (200, 200)  # (x, y)
color = (255, 0, 0)  # Blue color in BGR
thickness = 2
cv2.rectangle(image, start_point, end_point, color, thickness)

# Draw a circle
center = (300, 300)  # (x, y)
radius = 50
cv2.circle(image, center, radius, color, thickness)

# Add text annotation
font = cv2.FONT_HERSHEY_SIMPLEX
text = 'OpenCV Annotation'
org = (10, 500)  # (x, y)
fontScale = 1
fontColor = (0, 255, 0)  # Green
lineType = 2
cv2.putText(image, text, org, font, fontScale, fontColor, lineType)

# Save the annotated image
cv2.imwrite('annotated_image.jpg', image)