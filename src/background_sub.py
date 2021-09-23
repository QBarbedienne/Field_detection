import cv2
from d3dshot import display
import numpy as np
from matplotlib.pyplot import *


class FrameFocus():
    def __init__(self, image, init_params, field, fpsc):
        self.image = image
        self.image_bis = image.copy()
        self.terrain = field
        self.init_parameters = init_params
        self.problemos = False
        self.h = []
        self.coord = [0, 0, 0, 0]
        self.fpsc = fpsc
        self.find_ground()

    def remove_background(self):
        # Transfo de l'image en HSV (+ d'info sur le cylindre HSV sur google)
        hsv = cv2.cvtColor(self.image, cv2.COLOR_RGB2HSV)

        # Si les paramétres n'ont pas encore été trouvés.
        if self.init_parameters.paramTot[0] == 0:
            # On split pour ne s'interesser qu'a à la couleur
            h, _, _ = cv2.split(hsv)
            # Création d'un histogramme de l'image représentant la variation des couleurs
            hist = cv2.calcHist([h], [0], None, [90], [0, 90])
            # En dessous d'un valeur seuille, on vire (l'image d'un terrain de foot est souvent verte oui...)
            sigtab = np.where(np.array(
                [x/max(hist) for x in hist]) >= self.init_parameters.min_hist_line, 1, 0)
            # On selectionne la partie qui ressemble le + a du vert. En hsv, la valeur de  30 < h < 90 est du vert/jaune (au cas où le soleil vienne nous embêter) 
            paramin = np.argmax(sigtab)
            if paramin < 30:
                self.problemos = True
                # S'il y a un soucis, on baisse la vleur seuil de l'histogramme précédent
                if self.init_parameters.min_hist_line <= 0.2:
                    self.init_parameters.min_hist_line += 0.05
                else:
                    self.problemos = False
            else:
                self.problemos = False
            # On vire les grosses vérifications histoire d'avoir un résultat 'honnete' mais qui peut-être faux.
            # if paramin > 85 or paramin < 30:
            #     paramin = 30
            paramax = len(sigtab)-np.argmax(sigtab[::-1])
            # if paramax > 90 or paramax < 35:
            #     paramax = 90
            if paramax > 35 and paramax <= 90:
                self.init_parameters.paramTot[0] = int(paramin)
                self.init_parameters.paramTot[1] = int(paramax)
        if self.problemos == False:
            # Et pour finir, si l'initialisation est effecutée, on applique le filtre déduit sur l'ensemble de l'image.
            mask = cv2.inRange(hsv, (int(self.init_parameters.paramTot[0]), 30, 30), (int(
                self.init_parameters.paramTot[1]), 255, 255))
            self.green = cv2.bitwise_and(hsv, hsv, mask=mask)
            self.h, _, _ = cv2.split(self.green)

    def find_ground(self):
        # Find contours
        self.remove_background()
        if len(self.h) == 0:
            self.fpsc.count_calc()
            return
        contours, _ = cv2.findContours(
            self.h, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        Coord = [len(self.image), len(self.image[0]), 0, 0]
        self.mask_hsv = np.zeros(self.green.shape, np.uint8)
        if len(contours) > 1:
            cntsSorted = sorted(contours, key=lambda x: cv2.contourArea(x))
            # On étudies ici le cas où me terrain serait coupé en deux. Dans ces conditions on joint les deux "rectangles" trouvés ensembles.
            x, y, w, hi = cv2.boundingRect(cntsSorted[len(cntsSorted)-1])
            x2, y2, w2, _ = cv2.boundingRect(cntsSorted[len(cntsSorted)-2])
            if (y2+30 > y or y2-30 < y) and hi > len(self.h)/2:
                if x > x2:
                    if x-x2+w > w:
                        w = x-x2+w
                    x = x2
                else:
                    if x2-x+w2 > w:
                        w = x2-x+w2
                    x = x
            Coord = [x, y, w, hi]
        else:
            x, y, w, hi = Coord
        if w < (self.image.shape[1])/2 or hi < (self.image.shape[0]/2):
            self.skip()
            self.fpsc.count_calc()
            return
        if self.terrain.size[0] == 0 and self.terrain.size[1] == 0:
            self.terrain.size = [w, hi]
            self.terrain.coordinates = [x, y]
        elif self.terrain.size[0]*0.8 > w or w > self.terrain.size[0]*1.2 or self.terrain.size[1]*0.8 > hi or hi > self.terrain.size[1]*1.2:
            self.skip()
            self.fpsc.count_calc()
            return 
        else:
            self.terrain.size = [w, hi]
            self.terrain.coordinates = [x, y]
        if w ==0 and hi == 0:
            self.coord = [0,0,0,0]
        else:
            self.coord = [x, y, w, hi]
        self.fpsc.count_calc()
    
    def skip(self):           
        self.init_parameters.paramTot = [0, 0, 0, 0, 0]
        self.terrain.size = [0, 0]
        self.terrain.coordinates = [0, 0]
        self.coord = [0, 0, 0, 0]

    def display_ground(self):
        if len(self.h) == 0:
            self.mask_rgb = np.zeros(self.image.shape, np.uint8)
            self.mask_hsv = np.zeros(self.image.shape, np.uint8)
            return
        x, y, w, hi= self.coord
        self.mask_rgb = np.zeros(self.image.shape, np.uint8)
        self.mask_rgb[y:y+hi, x:x+w] = self.image[y:y+hi, x:x+w]
        self.image_bis = cv2.rectangle(self.image_bis, (x,y), (x+w, y+hi), (0,255,0), 2)
        if ((x+w)*(y+hi))*2 > (len(self.h)*len(self.h[0])):
            self.mask_hsv[y:y+hi, x:x+w] = self.green[y:y+hi, x:x+w]
