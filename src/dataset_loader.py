import cv2
import os
import glob

class DatasetLoader:


    def load_images(self, image_dir):

        im_list = []
        image_types = ["day", "night"]

        for im_type in image_types:

            for file in glob.glob(os.path.join(image_dir, im_type, "*")):

                im = cv2.imread(file)

                if not im is None:
                    im_list.append((im, im_type))

        return im_list
