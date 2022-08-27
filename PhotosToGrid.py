import os, cv2
import numpy as np

path = "Immagini/"
outputpath = "Output/"
estensioneoutput = "png"
maxrighe = 4
maxcolonne = 4
# 3508 x 2480 px A4
AltezzaFoglio = 3508
LarghezzaFoglio = 2480
Padding = 0

offsetAltezza = 0 #200
offsetLarghezza = 0 #150
#offsetAltezza = 200 #200
#offsetLarghezza = 150 #150
AltezzaImmagine = int((AltezzaFoglio - Padding )/ maxcolonne)
LarghezzaImmagine = int((LarghezzaFoglio - Padding) / maxrighe)
#LarghezzaImmagine = 708
#AltezzaImmagine = 1027

ImmagineFinale = np.ones((AltezzaFoglio-Padding,LarghezzaFoglio-Padding,3), np.uint8) * 255
V1 = [0,0] #vertice in alto a sinistra
V2 = [AltezzaImmagine,LarghezzaImmagine]  #vertice in basso a destra

ListaNomiImmagini = os.listdir(path)

dsize = (LarghezzaImmagine, AltezzaImmagine)
Riga = 0
Colonna = 0
Foglio = 1

for nomeImmagine in ListaNomiImmagini:
    immagine = cv2.imread(path + nomeImmagine)
    immagine = cv2.resize(immagine, dsize, interpolation = cv2.INTER_AREA)
    V1[0] = AltezzaImmagine*Riga+offsetAltezza
    V1[1] = AltezzaImmagine*(Riga+1) + offsetAltezza
    V2[0] = LarghezzaImmagine*Colonna + offsetLarghezza
    V2[1] = LarghezzaImmagine*(Colonna+1) + offsetLarghezza
    ImmagineFinale[V1[0]:V1[1], V2[0]:V2[1]] = immagine

    Colonna = (Colonna + 1) % maxcolonne
    if Colonna % maxrighe == 0:
        Riga += 1
        if Riga % maxrighe == 0:
            Riga = 0
            Colonna = 0
            cv2.imwrite(outputpath + "foglio_" + str(Foglio) + "." + estensioneoutput, ImmagineFinale)
            Foglio += 1
            ImmagineFinale = np.ones((AltezzaFoglio - Padding, LarghezzaFoglio - Padding, 3), np.uint8) * 255

cv2.imwrite(outputpath + "foglio_" + str(Foglio) + "." + estensioneoutput, ImmagineFinale)
print("fine")
