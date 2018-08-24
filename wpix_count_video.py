import numpy as np
import cv2
import matplotlib.pyplot as plt

def wpix_count(v_file):

  cap = cv2.VideoCapture(v_file)

  if (cap.isOpened()== False): 

    print("Error opening video stream or file")

  while(cap.isOpened()):

    ret , img1 = cap.read()

    img1_array = np.asarray(img1)

    img1_array[img1_array<215] = 0

    num_wpix = np.count_nonzero(img1_array)

    yield ret, num_wpix


