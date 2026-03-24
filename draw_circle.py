import cv2
import sys

image_path = r'C:\Users\Estefano\Desktop\Iro_colombia_final_final.jpeg'
image = cv2.imread(image_path)

if image is None:
    print("Error: No se encontró la imagen.")
    sys.exit()

# Círculo con borde (Rojo)
cv2.circle(image, (400, 400), 80, (0, 0, 255), 3)

# Círculo RELLENO (Amarillo/Cian)
cv2.circle(image, (200, 200), 50, (255, 255, 0), -1)

cv2.imshow("Demo: Drawing Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()