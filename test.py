from scipy.spatial.distance import euclidean
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2
import requests

# Function to show array of images (intermediate results)
# def show_images(images):
# 	for i, img in enumerate(images):
# 		cv2.imshow("image_" + str(i), img)
# 	cv2.waitKey(0)
# 	cv2.destroyAllWindows()

img_remove_bg = "images/tree.jpg"

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open(img_remove_bg, 'rb')},
    data={'size': 'preview', 'bg_color': 'fff'},
    headers={'X-Api-Key': 'GY6EVhsmUa1dWcyVCYntpqJ7'},
)
if response.status_code == requests.codes.ok:
    with open('images/result.jpg', 'wb') as out:
    	out.write(response.content)
else:
    print("Error:", response.status_code, response.text)