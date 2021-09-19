import cv2
import d3dshot

from src.caption import *
from src.parameters import *
from src.background_sub import *
from src.field import *
from src.fps import *
from src.keyevent import *

class Main():
    def __init__(self, value, ui):
        self.value = value
        self.read = True
        self.ui = []
        self.path_video = ''
        # Instanciation
        self.frame = OpenVideoFrame()
        self.init_param = InitialParameters()
        self.field = Terrain()
        self.fpsc = Fps()
        self.key_event = KeyEvent(self.init_param)
        #Génération du programme d'acquisition de l'écran
        self.img_previous = []
    
    def update(self, value, ui):
        self.value = value
        if self.value == False:
            self.ui = ui[0]
            self.read = ui[1]
            self.path_video = ui[2]
        else:
            self.read = True
            self.ui = []
            self.path_video = ''

    def start(self):
        if self.read :
            self.d = d3dshot.create(capture_output="numpy")
        else:
            self.frame.open_cap(self.path_video)
        while self.key_event.continue_while:
            # Acquisition de l'image + gestion de la pause
            if self.value:
                if self.read:
                    img = self.frame.get_real_time(self.d, self.fpsc)
                else:
                    img = self.frame.get_frame(self.fpsc)
            else:
                if self.ui.pause :
                    if len(self.img_previous) == 0:
                        if self.read:
                            img = self.frame.get_real_time(self.d, self.fpsc)
                        else:
                            img = self.frame.get_frame(self.fpsc)
                        self.img_previous = img.copy()
                    else:
                        self.fpsc.starting()
                        img = self.img_previous
                else:
                    if self.read:
                        img = self.frame.get_real_time(self.d, self.fpsc)
                    else:
                        img = self.frame.get_frame(self.fpsc)

            # Acquisition des évenemnts claviers
            self.key_event.update_key()

            # Acquisition du terrain (detection auto du vert+ découpage de l'image autour de cette zone)
            classes = FrameFocus(img, self.init_param, self.field, self.fpsc)

            # Gestion de l'image à afficher
            if self.value:
                if self.key_event.display == 0:
                    img = classes.image_bis
                elif self.key_event.display == 1:
                    img = classes.mask_hsv
                elif self.key_event.display == 2:
                    img = classes.mask_rgb
            else:
                if self.ui.event_display == 0:
                    img = classes.image_bis
                elif self.ui.event_display == 1:
                    img = classes.mask_hsv
                elif self.ui.event_display == 2:
                    img = classes.mask_rgb
            
            # reboot si UI, histoire de pas le faire rentrer dans les key events.
            if self.value == False and self.ui.reboot:
                self.ui.reboot = False
                self.init_param.reset()
            

            if self.value == False:
                self.ui.lineEdit.setText('%.2f' % (self.fpsc.fps_capture_mean))
                self.ui.lineEdit_2.setText('%.2f' % (self.fpsc.fps_mean))
                self.ui.update_frame(img)
            else:
                # Affichage des fps sur l'image. On le fait à la fin pour éviter de perturber le soft
                cv2.putText(img, 'calc = %.2f' % (self.fpsc.fps_mean), (0, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(img, 'max = %.2f' % (self.fpsc.fps_capture_mean), (0, 25),
                            cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.imshow('SC', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

            self.init_param.num_itteration += 1

        if self.value:
            print('fps max = %.2f'%self.fpsc.fps_capture_mean)
            print('fps totale = %.2f'%self.fpsc.fps_mean)

if __name__ == "__main__":
    main = Main(True, None)
    main.start()