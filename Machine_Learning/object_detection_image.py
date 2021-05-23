import os
import cv2

file_dir = os.path.abspath('')+"\\train"
file_path = os.path.join(file_dir, "cramorant.png")
image_file = cv2.imread(file_path)

cv2.imshow('image', image_file)
cv2.waitKey()
cv2.destroyAllWindows()