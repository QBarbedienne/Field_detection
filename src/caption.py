import cv2
import imutils
import numpy as np

np.seterr(divide='ignore', invalid='ignore')
np.warnings.filterwarnings('ignore')


class OpenVideoFrame():
    def __init__(self, link=''):
        self.link = link

    def get_real_time(self, d, fpsc):
        fpsc.starting()
        img_not_resize = d.screenshot()
        if len(img_not_resize) > 0:
            img = imutils.resize(img_not_resize, width=min(
                1280, img_not_resize.shape[1]))
        else:
            img = []
        fpsc.count_display()
        return img

    def open_cap(self, link):
        self.cap = cv2.VideoCapture(link)

    def get_frame(self, fpsc):
        fpsc.starting()
        _, img_not_resize = self.cap.read()
        if len(img_not_resize) > 0:
            img = imutils.resize(img_not_resize, width=min(1280, img_not_resize.shape[1]))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        else:
            img = []
        fpsc.count_display()
        # if self.init_params.pause:
        #     img = img_prev.copy()
        # else:
        #     self.init_params.Val, img_not_resize = self.cap.read()
        #     if self.init_params.Val:
        #         if img_not_resize.shape[1] < 1280:
        #             img = imutils.resize(img_not_resize, width=min(
        #                 1280, img_not_resize.shape[1]))
        #         else:
        #             img = img_not_resize
        #     else:
        #         img = []
        return img

    # def write_log(self, log_info, img):
    #     if self.init_params.Val and len(img) == 0:
    #         log_info.writeErrorLog('Program closed during the video process')
    #     elif not self.init_params.Val:
    #         log_info.write_info_log('Video ends')
