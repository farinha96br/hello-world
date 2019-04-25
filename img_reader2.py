import cv2
import numpy as np
import math as mt
import functions as fc
from matplotlib import pyplot as plt
import time
start = time.time()

#####################################################
##### TODAS AS FUNCOES RECEBEM O NOME DA IMAGEM #####
#####################################################
img = "imgs/Nbx/" + "13,5.bmp"
file = "mean-entropy.dat"
print(fc.img_info(img)) # informacoes da imagem

b = fc.col_vec(img,0)   # vetores dos canais RGB e G
g = fc.col_vec(img,1)
r = fc.col_vec(img,2)
gr = fc.gray_vec(img)

b_hist = np.histogram(b,range = (0,256),bins =  256, density = True)[0]  #histogramas de cada canal
g_hist = np.histogram(g,range = (0,256),bins =  256, density = True)[0]
r_hist = np.histogram(r,range = (0,256),bins =  256, density = True)[0]
gr_hist = np.histogram(gr,range = (0,256),bins =  256, density = True)[0]

#print(gr_hist)
#print("blue mean " + str(fc.mean(b)))   #printa as medias de cada cor + cinza
#print("green mean " + str(fc.mean(g)))
#print("red mean " + str(fc.mean(r)))
#print("gray mean " + str(fc.mean(gr)))
#fc.rgb_g_write("color.dat",img)  #escreve .dat com indice dos pixels e valores B R G
    #   Shannon entropy?
    #H(x) = \sum_{i=0}^{N-1}P_i log_2 p_i
S = (fc.entropy(img))

data = open(file,"w") # modo de escrita
data.write(str(fc.mean(b)) + " " + str(fc.mean(g)) + " " + str(fc.mean(r)) + " " + str(fc.mean(gr)) + " ")
data.write(str(S[0]) + " " + str(S[1]) + " " + str(S[2]) + " " + str(S[3]) + "\n")


end = time.time()







print("exe. time " + str(end - start) + " sec")

#cv2.imshow('gray',img_gray)
#cv2.imshow('color',img_color[0])
#cv2.waitKey(0) # espera uma tecla pra continuar o programa
#cv2.destroyAllWindows()
