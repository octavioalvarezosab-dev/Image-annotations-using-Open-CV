import cv2
import numpy as np

# Function to draw rectangles and annotations on an image

def draw_rectangles(image_path, rectangles, output_path):
    """
    Draws rectangles on the image and saves the annotated image.
    :param image_path: Path to the input image
    :param rectangles: List of rectangles to draw, each defined by a tuple
                      (x, y, width, height)
    :param output_path: Path to save the annotated image
    """
    # Read the image
    image = cv2.imread(image_path)
    
    for (x, y, width, height) in rectangles:
        # Draw the rectangle on the image
        cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)
        # Put a label (optional)
        cv2.putText(image, 'Rectangle', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Save the annotated image
    cv2.imwrite(output_path, image)

# Example of using the function
if __name__ == '__main__':
    image_path = 'input.jpg'
    output_path = 'output.jpg'
    rectangles = [(50, 50, 100, 100), (200, 80, 150, 150)]
    draw_rectangles(image_path, rectangles, output_path)
