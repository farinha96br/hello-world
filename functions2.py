import cv2
import numpy as np
import math as mt



#img = "rgb_test2.png" #nome do arquivo

# [OK] recebe o caminho da img e retorna o caminho e as propriedades
def img_info(file):
    img = cv2.imread(file,1)
    prop = img.shape
    return str(file) + " " + str(prop[0]) + "h " + str(prop[1]) + "w " + str(prop[2]) + "ch"

#[OK] recebe um vetor e retorna o valor medio do vetor numerico inserido
def mean(arg):
    return 1.0*sum(arg)/len(arg)

#[OK] recebe a matriz da imagem e retorna um vetor da cor com o canal escolhido
def col_vec(img,channel):
    prop = img.shape
    vec = []
    for row in range(0,prop[0]):
        for col in range(0,prop[1]):
            vec.append(img[row,col,channel])
    return vec

# [OK]  recebe a matriz da imagem e retorna o vertor da escala cinza
def gray_vec(img_gray):
    prop = img_gray.shape
    gray = []
    for row in range(0,prop[0]):
        for col in range(0,prop[1]):
            gray.append(img_gray[row,col])
    return gray

#[OK]   aceita uma string para o nome do arquivo a ser escrito
#       uma uma matrix de imagem RGB e uma matrix de imagem cinza
#       escreve entao um .dat com o indice de cada pixel e os valores
#       pixel R G B Gr
def rgb_g_write(file,img_color,img_gray):
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

def entropy(channel_vector):    #[OK] calcula entropia de um canal de cores
    hist = np.histogram(channel_vector,range = (0,256),bins =  256, density = True)[0]
    S = 0
    for i in range(0,len(hist)):
        if hist[i] > 0:
            S += -hist[i]*mt.log(hist[i])
    return S


############ coisas nao otimizadas daq pra baixo #####


#[OK]   recebe a matriz da imagem e retorna a cor me
def mean_color(img,channel):
    prop = img.shape
    vec = []
    for row in range(0,prop[0]):
        for col in range(0,prop[1]):
            vec.append(img[row,col,channel])
    return mean(vec)

#[OK]   retorna
def mean_gray(img):
    prop = img.shape
    vec = []
    for row in range(0,prop[0]):
        for col in range(0,prop[1]):
            vec.append(img[row,col])
    return mean(vec)
