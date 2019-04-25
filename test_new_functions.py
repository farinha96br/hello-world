import cv2
import numpy as np
import math as mt
import functions2 as fc2
import functions as fc


#####################################################
##### TODAS AS FUNCOES RECEBEM O NOME DA IMAGEM #####
#####################################################
img_file = "imgs/Nbx/" + "23,0.bmp"
img_color = cv2.imread(img_file,1)
img_gray = cv2.imread(img_file,0)
print(fc2.img_info(img_file))
print("b")
print(fc2.mean_color(img_color,0))
b = fc2.col_vec(img_color,0)
print(fc2.mean(b))
print("g")
print(fc2.mean_color(img_color,1))
g = fc2.col_vec(img_color,1)
print(fc2.mean(g))
print("r")
print(fc2.mean_color(img_color,2))
r = fc2.col_vec(img_color,2)
print(fc2.mean(r))
print("gr")
print(fc2.mean_gray(img_gray))
gr = fc2.gray_vec(img_gray)
print(fc2.mean(gr))

print(fc2.entropy(b))
print(fc.entropy(img_file)[0])
#fc2.rgb_g_write("teste2.dat",img_color,img_gray)












cv2.waitKey(0) # espera uma tecla pra continuar o programa
cv2.destroyAllWindows()

#file = "mean-entropy.dat"
#print(fc.img_info(img)) # informacoes da imagem

#b = fc.col_vec(img,0)   # vetores dos canais RGB e G
#g = fc.col_vec(img,1)
#r = fc.col_vec(img,2)
#gr = fc.gray_vec(img)







#cv2.imshow('gray',img_gray)
