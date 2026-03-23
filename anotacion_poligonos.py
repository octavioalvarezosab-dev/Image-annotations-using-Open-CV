import cv2
import numpy as np

# Function to draw polygons on an image
# The function takes an image and a list of points defining the polygon

def draw_polygon(image, points, color=(0, 255, 0), thickness=2):
    """Draws a polygon on the provided image."""
    points = np.array(points, np.int32)
    points = points.reshape((-1, 1, 2))
    cv2.polylines(image, [points], isClosed=True, color=color, thickness=thickness)
    return image

# Function to add annotations to an image

def annotate_image(image_path, polygons):
    """Annotates an image with polygons defined in the polygons list."""
    image = cv2.imread(image_path)
    
    for polygon in polygons:
        draw_polygon(image, polygon['points'], color=polygon.get('color', (0, 255, 0)), thickness=polygon.get('thickness', 2))
    
    # Show the image with annotations
    cv2.imshow('Annotated Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  

# Example Usage
if __name__ == '__main__':
    # Define polygons for annotation
    polygons = [
        {'points': [(100, 100), (200, 100), (200, 200), (100, 200)], 'color': (255, 0, 0)},
        {'points': [(300, 300), (400, 300), (400, 400), (300, 400)], 'color': (0, 0, 255)}
    ]
    
    # Annotate the image
    annotate_image('input_image.jpg', polygons)