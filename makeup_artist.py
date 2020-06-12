from PIL import Image
import os
from heartrate import heartrate


class Makeup_artist(object):
    def __init__(self):
        pass

    def apply_makeup(self, img):
    	heartrate()
        return img.transpose(Image.FLIP_TOP_BOTTOM) #invert img
        
