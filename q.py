import cv2
import numpy as np
def nothing(x):
	pass
	# tạo trackbars
cv2.namedWindow("Trackbars")
cv2.createTrackbar("H_min","Trackbars",0,170,nothing)
cv2.createTrackbar("S_min","Trackbars",0,255,nothing)
cv2.createTrackbar("V_min","Trackbars",0,255,nothing)
cv2.createTrackbar("H_max","Trackbars",170,170,nothing)
cv2.createTrackbar("S_max","Trackbars",255,255,nothing)
cv2.createTrackbar("V_max","Trackbars",255,255,nothing)
while True :
	# Đọc hình ảnh
	image=cv2.imread("14.jpg")
	# thay đổi kích thước ảnh
	image=cv2.resize(image,(600,600))
	# chuyển đổi không gian màu
	hsv=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
	# nhận giá trị Trackbars
	H_min=cv2.getTrackbarPos("H_min","Trackbars")
	S_min=cv2.getTrackbarPos("S+min","Trackbars")
	V_min=cv2.getTrackbarPos("V_min","Trackbars")
	H_max=cv2.getTrackbarPos("H_max","Trackbars")
	S_max=cv2.getTrackbarPos("S_max","Trackbars")
	V_max=cv2.getTrackbarPos("V_max","Trackbars")
	# phạm vi màu
	lower_red=np.array([H_min, S_min, V_min])
	upper_red=np.array([H_max, S_max, V_max])
	# biến đổi hình thái mở đầu và kết thúc
	thresh=cv2.inRange(hsv,lower_red,upper_red)
	kernel=np.ones((5,5),np.uint8)
	mask=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)
	mask=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
	result=cv2.bitwise_and(image,image,mask=mask)
	cv2.imshow("result", result)
	cv2.imwrite("test.jpg", result)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
print('okeeeeeeeeeee')
# xác định chiều dài
import cv2
import numpy as np
import math
image = cv2.imread("14.jpg")
image = cv2.resize(image,(600,600))
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
lower_red = np.array([1,11,32])
upper_red = np.array([15,255,255])
thresh = cv2.inRange(hsv,lower_red,upper_red)
kernel = np.ones((5,5),"uint8")
mask = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)
mask = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
result = cv2.bitwise_and(image,image,mask = mask)
cv2.imwrite("test.jpg",result)
img2 = cv2.imread("test.jpg",0)
# img3 = cv2.GaussianBlur(img2,(5,5),0)
print(img2)
# cv2.imshow(img2)
img3 = cv2.GaussianBlur(img2,(5,5),0)
duachuot = cv2.Canny(img3,100,200)
cv2.imshow("test.jpg",result)
cv2.imwrite("test.jpg",duachuot)
x = 0
y = 0
i = 0
j = 0
X = []
Y = []
P = []
L0 = 17.2
D = 463.4317641249896
for x in range(600):
	for y in range(600):
		px = duachuot[x][y]
		if px !=0:
			X.append(x)
			Y.append(y)
n = len(str(x))
m = len(str(y))
print(n)
for i in range(n):
	for j in range(m):
		khoangcach = ((X[i]- X[j])**2 + (Y[i]- Y[j])**2)
		d = math.sqrt(khoangcach)
		P.append(d)
l = (max(P)*L0)/D
print('dmax=',max(P))
print('kichthuocduachuot=',l)
cv2.waitKey(0)
cv2.destroyAllWindows()