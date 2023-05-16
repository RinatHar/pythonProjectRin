import os

import cv2
import numpy as np
from PIL import Image, ImageFilter
from math import sqrt

RESIZE = 5


class Scanner:
    def __init__(self, path):
        self.images_path = path
        self.dot_size = 1

    def find_dists(self):
        dists = []
        for file in os.listdir(self.images_path):
            self.select_points(os.path.join(self.images_path, file), dists)
        return dists

    def select_points(self, path, dists):
        image = Image.open(path)
        r, g, b = image.split()
        resize = self.resize_image(r)
        self.dist_center(resize, dists)

    def resize_image(self, image):
        (x, y) = image.size
        resized_image = image.resize((x//RESIZE, x//RESIZE))
        nparray = np.array(resized_image)
        for i in range(len(nparray)):
            for j in range(len(nparray[0])):
                if nparray[i][j] != 255 and nparray[i][j] > 165:
                    nparray[i][j] = 255
        image = Image.fromarray(nparray)
        return image

    def dist_center(self, image, dists):
        (x, y) = image.size
        center_x = x//2
        center_y = y//2

        nparray = np.array(image)
        for i in range(len(nparray)):
            for j in range(len(nparray[0])):
                if nparray[i][j] != 255:
                    dist = round(sqrt((center_x-i)**2 + (center_y-j)**2), 2)
                    dists.append(dist*RESIZE)







