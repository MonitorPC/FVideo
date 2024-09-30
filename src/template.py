class ImageData:
    """Represents the data flowing through the pipeline"""

    def __init__(self, image, cur_image):
        self.image = image  # Always store the original image as RGB
        self.cur_image = cur_image  # Store the last filtered image


class Pipe:
    """Represents a pipe that holds ImageData and handles input/output."""

    def __init__(self):
        self.data = None

    def put(self, data: ImageData):
        self.data = data

    def get(self) -> ImageData:
        return self.data


class Filter:
    """Abstract base class for filters that operate on a single Pipe."""

    def __init__(self, pipe: Pipe):
        self.pipe = pipe

    def process(self):
        """Processes the image in the pipe."""
        data = self.pipe.get()

        # ... perform processing on data.cur_image ...

        self.pipe.put(data)  # Write the processed data back to the pipe 