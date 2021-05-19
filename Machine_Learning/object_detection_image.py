import os
import numpy as np
import tensorflow as tf
import sys
import cv2
import pytesseract

file_dir = os.path.abspath('')+"\\Resources"
file_path = os.path.join(file_dir, "cramorant.png")
print(file_path)
image_file = cv2.imread()