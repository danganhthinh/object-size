"""
Filename: init.py
Usage: This script will measure different objects in the frame using a reference object of known dimension. 
The object with known dimension must be the leftmost object.
Author: Shashank Sharma
"""
from scipy.spatial.distance import euclidean
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2
import requests

# Function to show array of images (intermediate results)
def show_images(images):
	for i, img in enumerate(images):
		cv2.imshow("image_" + str(i), img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
# ảnh cần đo
img_input = "images/input.jpg"

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open(img_input, 'rb')},
    data={'size': 'auto', 'bg_color': 'fff'},
    headers={'X-Api-Key': 'GY6EVhsmUa1dWcyVCYntpqJ7'},
)
if response.status_code == requests.codes.ok:
    with open('images/img_result_remove_bg.jpg', 'wb') as out:
    	out.write(response.content)
else:
    print("Error:", response.status_code, response.text)

img_result_remove_bg = 'images/img_result_remove_bg.jpg'

img_result_remove_bg = cv2.imread(img_result_remove_bg, 1)

cv2.line(img_result_remove_bg, (24,18), (24,63), (255,0,0), 3)
cv2.line(img_result_remove_bg, (87,17), (87,63), (255,0,0), 3)
cv2.line(img_result_remove_bg, (24,18), (87,17), (255,0,0), 3)
cv2.line(img_result_remove_bg, (87,63), (24,63), (255,0,0), 3)

cv2.imwrite('images/img_input_remove_bg.jpg', img_result_remove_bg)
img_path = 'images/img_input_remove_bg.jpg'

# img_path = "images/tree4.png"
# img_path = "images/tree.jpg"

# Read image and preprocess
image = cv2.imread(img_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (9, 9), 0)

# edged = cv2.Canny(blur, 50, 100)
edged = cv2.Canny(blur, 100, 120)
edged = cv2.dilate(edged, None, iterations=1)
edged = cv2.erode(edged, None, iterations=1)

show_images([blur, edged])

# Find contours
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# Sort contours from left to right as leftmost contour is reference object
(cnts, _) = contours.sort_contours(cnts)

# Remove contours which are not large enough
cnts = [x for x in cnts if cv2.contourArea(x) > 100]

#cv2.drawContours(image, cnts, -1, (0,255,0), 3)

#show_images([image, edged])
#print(len(cnts))

# Reference object dimensions
# Here for reference I have used a 2cm x 2cm square
ref_object = cnts[0]
box = cv2.minAreaRect(ref_object)
box = cv2.boxPoints(box)
box = np.array(box, dtype="int")
box = perspective.order_points(box)
(tl, tr, br, bl) = box
dist_in_pixel = euclidean(tl, tr)
dist_in_cm = 11.3
pixel_per_cm = dist_in_pixel/dist_in_cm

# Draw remaining contours
for cnt in cnts:
	box = cv2.minAreaRect(cnt)
	box = cv2.boxPoints(box)
	box = np.array(box, dtype="int")
	box = perspective.order_points(box)
	(tl, tr, br, bl) = box
	cv2.drawContours(image, [box.astype("int")], -1, (0, 0, 255), 2)
	mid_pt_horizontal = (tl[0] + int(abs(tr[0] - tl[0])/2), tl[1] + int(abs(tr[1] - tl[1])/2))
	mid_pt_verticle = (tr[0] + int(abs(tr[0] - br[0])/2), tr[1] + int(abs(tr[1] - br[1])/2))
	wid = euclidean(tl, tr)/pixel_per_cm
	ht = euclidean(tr, br)/pixel_per_cm
	cv2.putText(image, "{:.1f}cm".format(wid), (int(mid_pt_horizontal[0] - 15), int(mid_pt_horizontal[1] - 10)),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
	cv2.putText(image, "{:.1f}cm".format(ht), (int(mid_pt_verticle[0] + 10), int(mid_pt_verticle[1])),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

show_images([image])