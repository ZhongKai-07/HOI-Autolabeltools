import cv2
from PIL import Image
import numpy as np

class Common:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def Scale(img, target_sz=(768, 1024)):
        shape = np.shape(img)[0:2]
        if isinstance(target_sz, int):
            new_sz = (target_sz, int(target_sz*3/4))
        ratio = min(target_sz[0] / shape[0], target_sz[1] / shape[1])
        new_unpad = (int(shape[0] * ratio), int(shape[1] * ratio))
        if shape != new_unpad:
            #img = img.resize((new_unpad[1], new_unpad[0]), Image.ANTIALIAS)
            img = cv2.resize(img, (new_unpad[1], new_unpad[0]), interpolation=cv2.INTER_LINEAR)
        return img

    @staticmethod
    def yolo_format_str(classes, xmin, ymin, w, h):
        save_label = str(classes) + " " + str(xmin) + " " + str(ymin) + " " + str(w) + " " + str(h)
        return save_label

    @staticmethod
    def save_label_parse(save_label):
        classes, xmin, ymin, w, h = save_label.split(" ")
        return int(classes), float(xmin), float(ymin), float(w), float(h)