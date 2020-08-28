import cv2

img = cv2.imread('/images/tree.jpg', 0)
img2 = cv2.Canny(img, 200, 255)

cv2.imshow('tree', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()