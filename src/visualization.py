import matplotlib.pyplot as plt
import numpy as np
import cv2

class Visualization:


    def plot_images(self, images_list):


        some_images = images_list[:6] + images_list[-6:]

        fig = plt.figure(figsize=(12, 15))

        pos = 1
        for im, im_type in some_images:

            fig.add_subplot(4, 3, pos)
            pos += 1
            fig.tight_layout(pad=1.0)
            im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            plt.imshow(im)
            plt.axis('off')
            plt.title("Label: "+im_type+
                    "\nImage Shape: "+str(im.shape))


    def plot_data_distribution(self, y_train, y_test):

        values, counts = np.unique(y_train, return_counts=True)
        _, counts_t = np.unique(y_test, return_counts=True)

        X_axis = np.arange(len(values))

        plt.bar(X_axis - 0.2, counts, 0.4, label = 'Train data')
        plt.bar(X_axis + 0.2, counts_t, 0.4, label = 'Test data')

        plt.xlabel('Label')
        plt.ylabel('Quantidade de imagens')
        plt.xticks(X_axis, ('day', 'night'))

        plt.title("Quantidade de imagens")
        plt.legend()
        plt.show()
