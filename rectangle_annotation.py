import cv2
import numpy as np

# Function to draw and annotate rectangles on an image

def draw_rectangle(image_path, start_point, end_point, color=(255, 0, 0), thickness=2, annotation_text=''):
    # Read the image
    image = cv2.imread(image_path)
    
    # Draw a rectangle on the image
    cv2.rectangle(image, start_point, end_point, color, thickness)
    
    # Annotate the rectangle with text
    if annotation_text:
        # Calculate text size for centering
        (w, h), _ = cv2.getTextSize(annotation_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        cv2.putText(image, annotation_text, (start_point[0], start_point[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    
    # Display the image with the rectangle and annotation
    cv2.imshow('Annotated Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
if __name__ == '__main__':
    draw_rectangle('path/to/image.jpg', (50, 50), (200, 200), color=(0, 255, 0), thickness=3, annotation_text='My Rectangle')
