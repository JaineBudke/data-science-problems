import cv2
import numpy as np


class FeatureExtraction:



    def brightness_value(self, img):
        hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

        v_values = np.sum(hsv_img[:, :, 2])
        area = img.shape[0] * img.shape[1]

        avg_brightness = v_values/area

        return avg_brightness


    def extract_all_brightness(self, images):

        brig = []
        for image in images:
            brig.append(self.brightness_value(image))

        return brig
