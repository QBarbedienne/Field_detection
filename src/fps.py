import numpy as np
import time

class Fps():
    def __init__(self):
        self.fps = [30, 30]
        self.fps_capture = [30, 30]
        self.fps_mean = 30
        self.fps_capture_mean = 30
        self.nbr_save = 100

    def starting(self):
        self.start = time.time()
    
    def count_display(self):
        end_c = time.time()
        seconds_c = end_c - self.start
        if len(self.fps_capture) > self.nbr_save:
            del self.fps_capture[0]
        self.fps_capture.append(1/seconds_c)
        self.fps_capture_mean = np.mean(self.fps_capture)

    def count_calc(self):
        end_c = time.time()
        seconds_c = end_c - self.start
        if len(self.fps) > self.nbr_save:
            del self.fps[0]
        self.fps.append(1/seconds_c)
        self.fps_mean=np.mean(self.fps)