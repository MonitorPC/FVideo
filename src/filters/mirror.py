import cv2
from template import Filter, ImageData


class MirrorFilter(Filter):
    """Flips the input frame horizontally."""

    def process(self):
        data = self.pipe.get()
        flipped = cv2.flip(data.image, 1)
        self.pipe.put(ImageData(flipped)) 