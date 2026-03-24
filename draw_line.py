import cv2
import sys

image_path = r'C:\Users\Estefano\Desktop\Iro_colombia_final_final.jpeg'
image = cv2.imread(image_path)

if image is None:
    print("Error: No se encontró la imagen.")
    sys.exit()

cv2.line(image, (100, 100), (500, 500), (255, 0, 0), 5)
cv2.line(image, (100, 600), (800, 600), (0, 255, 0), 3, cv2.LINE_AA)

cv2.imshow("Demo: Drawing Lines", image)
cv2.waitKey(0)
