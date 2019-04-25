import cv2
import numpy as np
import math as mt
import functions2 as fc
from matplotlib import pyplot as plt
import time
import os
start = time.time()

#####################################################
##### TODAS AS FUNCOES RECEBEM O NOME DA IMAGEM #####
#####################################################

entropy_file = open("entropy.dat","w") # modo de escrita

cap = cv2.VideoCapture('videos/pitty.mp4')
i = 1
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    S = fc.entropy(gray)
    entropy_file.write(str(i) + " " + str(S) + "\n")
    print(S)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i = i + 1

cap.release()
cv2.destroyAllWindows()

entropy_file.close
