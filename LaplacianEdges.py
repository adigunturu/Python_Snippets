import cv2
import numpy as np

img = cv2.imread("hello.jfif")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,  cv2.THRESH_BINARY, 9, 9)


color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)
blur = cv2.GaussianBlur(img, (3, 3), 3)
laplacian = cv2.Laplacian(blur, cv2.CV_64F)
cv2.imshow("cuteKoala", img)
cv2.imshow("Filter", laplacian)
##cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
