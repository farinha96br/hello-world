import cv2
import numpy as np
import math as mt

#img = "rgb_test2.png" #nome do arquivo

def img_info(img):
    img2 = cv2.imread(img,1)
    prop = img2.shape
    return img + " " + str(prop[0]) + "h " + str(prop[1]) + "w " + str(prop[2]) + "ch"

def mean(arg):                  # retorna o valor medio de uma lista numerica [ OK ]
    return 1.0*sum(arg)/len(arg)

def mean_color(img,channel):    # retorna a cor media da img no canal pedido
    img = cv2.imread(img,1)
    prop = img.shape
    vec = []
    for row in range(0,prop[0]):
        for col in range(0,prop[1]):
            vec.append(img[row,col,channel])
    return mean(vec)

def mean_gray(img):
    img = cv2.imread(img,0)
    prop = img.shape
    vec = []
    for row in range(0,prop[0]):
        for col in range(0,prop[1]):
            vec.append(img[row,col])
    return mean(vec)



def col_vec(img,channel):
    img = cv2.imread(img,1)
    prop = img.shape
    vec = []
    for row in range(0,prop[0]):
        for col in range(0,prop[1]):
            vec.append(img[row,col,channel])
    return vec

def col_vec_all(img):       #retorna uma matriz com os vetors [[B],[G],[R]]
    img_color = cv2.imread(img,1)
    prop = img_color.shape
    blue = []
    green = []
    red = []
    for row in range(0,prop[0]):
        for col in range(0,prop[1]):
            blue.append(img_color[row,col,0])
            green.append(img_color[row,col,1])
            red.append(img_color[row,col,2])
    return [blue,green,red]

#print(col_vec_all("rgb_test2.png")[0])

def gray_vec(img):       #retorna o vetor da escala cinza
    img_color = cv2.imread(img,0)
    prop = img_color.shape
    gray = []
    for row in range(0,prop[0]):
        for col in range(0,prop[1]):
            gray.append(img_color[row,col])
    return gray

def rgb_g_write(file,img): # gera um .dat com o indice dos pixels e seus valores RGB
    img_color = cv2.imread(img,1)
    img_gray = cv2.imread(img,0)
    data = open(file,"w") # modo de escrita
    prop = img_color.shape
    pixel=0
    for row in range(0,prop[0]):
        for col in range(0,prop[1]):
            data.write(str(pixel) + " ") # escreve indice do pixel
            data.write(str(img_color[row,col,0]) + " ") # escreve o canal B
            data.write(str(img_color[row,col,1]) + " ") # escreve o canal G
            data.write(str(img_color[row,col,2]) + " ") # escreve p canal R e pula p proxima linha
            data.write(str(img_gray[row,col]) + "\n")
            pixel += 1
        pixel += 1
    data.close()

def entropy(img_file):
    b = col_vec(img_file,0)   # vetores dos canais RGB e G
    g = col_vec(img_file,1)
    r = col_vec(img_file,2)
    gr = gray_vec(img_file)
    b_hist = np.histogram(b,range = (0,256),bins =  256, density = True)[0]  #histogramas de cada canal
    g_hist = np.histogram(g,range = (0,256),bins =  256, density = True)[0]
    r_hist = np.histogram(r,range = (0,256),bins =  256, density = True)[0]
    gr_hist = np.histogram(gr,range = (0,256),bins =  256, density = True)[0]
    S_b = 0
    S_g = 0
    S_r = 0
    S_gr = 0
    for i in range(0,len(g_hist)):
        if b_hist[i] > 0:
            S_b += -b_hist[i]*mt.log(b_hist[i])
        if g_hist[i] > 0:
            S_g += -g_hist[i]*mt.log(g_hist[i])
        if r_hist[i] > 0:
            S_r += -r_hist[i]*mt.log(r_hist[i])
        if gr_hist[i] > 0:
            S_gr += -gr_hist[i]*mt.log(gr_hist[i])
    return [S_b,S_g,S_r,S_gr]
