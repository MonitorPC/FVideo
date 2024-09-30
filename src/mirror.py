import cv2
from template import Filter, ImageData

class MirrorFilter(Filter):
    """Flips the input frame horizontally."""

    def process(self):
        data = self.pipe.get()
        flipped = cv2.flip(data.cur_image, 1)
        self.pipe.put(ImageData(data.image, flipped)) 