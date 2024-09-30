import cv2
import numpy as np
from template import Filter, ImageData

class RnBFilter(Filter):
    """Applies a red and blue filter to the input frame."""

    def process(self):
        data = self.pipe.get()
        b, g, r = cv2.split(data.image)
        g = np.zeros_like(g)
        merged = cv2.merge((b, g, r))
        self.pipe.put(ImageData(merged)) 