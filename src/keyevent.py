import cv2

class KeyEvent():
    def __init__(self, init_params):
        self.continue_while = True
        self.init_params = init_params
        self.display = 0

    def update_key(self):
        self.value_key = cv2.waitKey(1)

        if self.value_key == ord('q'):
            self.continue_while = False
        elif self.value_key == ord('r'):
            self.init_params.reset()
        elif self.value_key == ord('o'):
            if self.display < 2:
                self.display += 1
            else:
                self.display = 0