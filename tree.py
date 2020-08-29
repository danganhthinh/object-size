import cv2

img = cv2.imread('images/example_02.jpg', 1)
# 24,18
# 24,63
#
# 87,17
# 87,63
#
# 24,18
# 87,17
#
# 87,63
# 24,63

cv2.line(img, (24,18), (24,63), (255,0,0), 3)
cv2.line(img, (87,17), (87,63), (255,0,0), 3)
cv2.line(img, (24,18), (87,17), (255,0,0), 3)
cv2.line(img, (87,63), (24,63), (255,0,0), 3)

cv2.imwrite('draw_img.jpg', img)

# cv2.imshow('tree', 'draw_img.jpg')
cv2.waitKey(0)
cv2.destroyAllWindows()