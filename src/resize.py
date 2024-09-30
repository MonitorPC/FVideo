import cv2
from template import Filter, ImageData

class ResizeFilter(Filter):
    """Resizes the input frame."""

    def __init__(self, pipe, width=320, height=240):
        super().__init__(pipe)
        self.width = width
        self.height = height

    def process(self):
        data = self.pipe.get()
        resized = cv2.resize(data.cur_image, (self.width, self.height))
        self.pipe.put(ImageData(data.image, resized))