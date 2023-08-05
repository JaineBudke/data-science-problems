import cv2
import numpy as np


class Preprocessing:


    def standardize_image(self, image, size):

        std_img=  cv2.resize(image, size)
        return std_img

    def encode_label(self, label):

        if label == 'day':
            return 0
        else:
            return 1

    def standardize_inputs(self, img_list, size):

        std_list = []

        for img in img_list:
            std_img = self.standardize_image(img[0], size)
            std_label = self.encode_label(img[1])

            std_list.append((std_img, std_label))

        return std_list

    def split_data(self, data):

        X, y = [], []
        for item in data:
            X.append(item[0])
            y.append(item[1])

        return X, y

    def split_features_labels(self, train_data, test_data):


        X_train, y_train = self.split_data(train_data)
        X_test, y_test   = self.split_data(test_data)

        return X_train, y_train, X_test, y_test

    def prepare_input(self, data):

        return np.array(data).reshape(-1, 1)
