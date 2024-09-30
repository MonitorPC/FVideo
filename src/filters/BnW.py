import cv2
from template import Filter, ImageData


class BnWFilter(Filter):
    """Converts input frame to black and white."""

    def process(self):
        data = self.pipe.get()
        gray = cv2.cvtColor(data.image, cv2.COLOR_BGR2GRAY)
        rgb_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        self.pipe.put(ImageData(rgb_image))