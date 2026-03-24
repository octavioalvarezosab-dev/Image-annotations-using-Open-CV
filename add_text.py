import cv2
import sys

image_path = r'C:\Users\Estefano\Desktop\Iro_colombia_final_final.jpeg'
image = cv2.imread(image_path)

if image is None:
    print("Error: No se encontró la imagen.")
    sys.exit()

# TEXTO 1: Etiqueta simple
cv2.putText(image, 'AIROS', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

cv2.imshow("Demo: Adding Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()