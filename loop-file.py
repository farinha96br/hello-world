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
directory = "imgs/Nbx/"

i = 1

entropy_file = open("entropy.dat","w") # modo de escrita
mean_file = open("mean.dat","w")
variance_file = open("variance.dat","w")

for filename in sorted(os.listdir(directory)):  #loopa os arquivos na pasta que tem as imgs
    if filename.endswith(".bmp"):   # pega as imgs com tal extensao
        img_color = cv2.imread(directory + filename,1)
        img_gray = cv2.imread(directory + filename,0)
        print(fc.img_info(directory + filename) + " " + str(i))
        T = os.path.splitext(filename)[0]

        b = fc.col_vec(img_color,0)
        g = fc.col_vec(img_color,1)
        r = fc.col_vec(img_color,2)
        gr = fc.gray_vec(img_gray)

        entropy_file.write( T + " " +\
        str(fc.entropy(b)) + " " +\
        str(fc.entropy(g)) + " " +\
        str(fc.entropy(r)) + " " +\
        str(fc.entropy(gr)) + "\n")




entropy_file.close
mean_file.close
variance_file.close







#img = "imgs/Nbx/" + "13,5.bmp"
#file = "mean-entropy.dat"
#print(fc.img_info(img)) # informacoes da imagem


end = time.time()






print("exe. time " + str(end - start) + " sec")

#cv2.imshow('gray',img_gray)
#cv2.imshow('color',img_color[0])
#cv2.waitKey(0) # espera uma tecla pra continuar o programa
#cv2.destroyAllWindows()
