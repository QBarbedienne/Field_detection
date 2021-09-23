import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QLabel,
                             QMainWindow, QMessageBox)
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtGui import QImage
from PyQt5.uic import loadUi

from ui.first import *
from ui.second import *
from main import *


class Ui_Display_bis(QMainWindow, Ui_Display):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.init_image_display()
        self.main = Main(False, [self, parent.direct_capture, parent.path_video])
        self.connect_signals_slots()
        self.event_display = 0
        self.reboot = False
        self.pause = False
        self.quit = True

    def init_image_display(self):
        # Aucune interet ici.. c'est seulement histoire de voir si ça fonctionne bien et si j'arrive à bien choper mon widget d'affichage
        self.image_plot = QLabel(self)
        grey = QPixmap(801, 461)
        grey.fill(QColor('darkGray'))
        self.image_plot.setPixmap(grey)
        self.verticalLayout.addWidget(self.image_plot)
        grey = QPixmap(801, 461)
        grey.fill(QColor('darkGray'))
        self.image_plot.setPixmap(grey)

    def connect_signals_slots(self):
        self.pushButton.clicked.connect(self.start_main)
        self.pushButton_4.clicked.connect(self.quit)
        self.pushButton_5.clicked.connect(self.change_view)
        self.pushButton_3.clicked.connect(self.reboot)
        self.pushButton_2.clicked.connect(self.pause)

    def start_main(self):
        # d3dshot fait chier avec le reboot...
        # self.main = Main(False, [self, parent.direct_capture])
        self.main.update(False, [self, self.parent.direct_capture, self.parent.path_video])
        self.main.start()

    def pause(self):
        if self.pause :
            self.pause = False
        else:
            self.pause = True

    def quit(self):
        self.quit = False
        self.parent.show()
        cv2.destroyAllWindows()
        self.close()

    def update_frame(self, frame):
        frame = cv2.resize(frame.copy(), (801, 461),
                           interpolation=cv2.INTER_AREA)
        self.fieldo = frame
        image = QImage(self.fieldo, self.fieldo.shape[1], self.fieldo.shape[0], int(
            3*self.fieldo.shape[1]), QImage.Format_RGB888)
        # Commenté pour le moment.. Ca peut-être utile si jamais on veut afficher des "images" qui n'en sont pas vraiment
        # else:
        #     image = qimage2ndarray.array2qimage(frame)
        self.image_plot.setPixmap(QPixmap.fromImage(image))

    def change_view(self):
        if self.event_display < 2:
            self.event_display += 1
        else:
            self.event_display = 0
    
    def reboot(self):
        self.reboot = True


class Window(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.real_time = True
        self.direct_capture = True
        self.path_video = ''
        self.setupUi(self)
        self.display_field = Ui_Display_bis(self)
        self.connect_signals_slots()

    def connect_signals_slots(self):
        self.pushButton.clicked.connect(self.open_display)
        self.pushButton_2.clicked.connect(self.open_display_read)

    def open_display(self):
        self.direct_capture = True
        self.real_time = True
        self.close()
        self.display_field.show()

    def open_display_read(self):
        dialog = QFileDialog()
        foo_dir = dialog.getOpenFileName(self, 'Select file')
        if 'avi' in foo_dir[0] or 'mp4' in foo_dir[0] or 'mkv' in foo_dir[0] or 'm4v' in foo_dir[0] or 'mov' in foo_dir[0]:
            self.direct_capture = False
            self.path_video = foo_dir[0]
            self.close()
            self.display_field.show()
        else:
            print('impossible to read video')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
    
