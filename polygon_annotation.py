import cv2
import numpy as np

class PolygonAnnotation:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        self.clone = self.image.copy()
        self.points = []
        self.drawing = False

    def draw_polygon(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.points.append((x, y))
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing:
                self.clone = self.image.copy()
                cv2.polylines(self.clone, [np.array(self.points + [(x, y)])], isClosed=False, color=(0, 255, 0), thickness=2)
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            cv2.polylines(self.clone, [np.array(self.points + [(x, y)])], isClosed=False, color=(0, 255, 0), thickness=2)

    def show_image(self):
        cv2.namedWindow('Polygon Annotation')
        cv2.setMouseCallback('Polygon Annotation', self.draw_polygon)

        while True:
            cv2.imshow('Polygon Annotation', self.clone)
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # Esc key to exit
                break
            elif key == ord('c'):  # 'c' to clear the drawing
                self.points = []
                self.clone = self.image.copy()

        cv2.destroyAllWindows()

if __name__ == '__main__':
    annotator = PolygonAnnotation('path_to_your_image.jpg')  # Replace with your image path
    annotator.show_image()