## Real-time Video Processing Pipeline

#### Implementation based on *Pipes&Filters* architecture


This project demonstrates the Pipes and Filters architectural pattern for real-time video processing using OpenCV in Python. 

### Project Structure

- **`template.py`:** Contains the core classes for the pipeline:
    - `ImageData`: Represents the image data (original and processed) flowing through the pipeline.
    - `Pipe`: A pipe that holds `ImageData` and manages data input/output for filters.
    - `Filter`: Abstract base class for all image processing filters.
- **`BnW.py`:** Implements a black and white filter.
- **`mirror.py`:** Implements a horizontal mirror filter.
- **`resize.py`:** Implements an image resizing filter.
- **`RnB.py`:** Implements a red and blue color filter.
- **`main.py`:** The main application that sets up the pipeline and processes video frames.

### How it Works

1. **`ImageData`:**  This class encapsulates the image data. It stores:
   - `image`: The original RGB image.
   - `cur_image`: The image resulting from the last filter applied.

2. **`Pipe`:**  A `Pipe` object acts as a conduit between filters. It holds the current `ImageData` being processed. Filters read input from and write output to the `Pipe`.

3. **`Filter`:** All filters inherit from the `Filter` base class. Each filter implements a `process()` method, which:
   - Gets the current `ImageData` from the pipe.
   - Processes the `cur_image` within the `ImageData` object.
   - Puts the modified `ImageData` back into the pipe.

4. **`main.py`:**
   - Sets up the video capture (from webcam or file).
   - Creates a `Pipe` object.
   - Instantiates the filters, passing the `Pipe` to each.
   - Enters a loop:
     - Reads a frame from the video source.
     - Creates an `ImageData` object and puts it into the pipe.
     - Calls the `process()` method of each filter in sequence.
     - Retrieves the processed `ImageData` from the pipe.
     - Displays the final processed frame.

### How to Run

1. **Install OpenCV:** `pip install opencv-python`
2. **Run `main.py`:** `python main.py`

This will start the application and display the processed video stream. Press the `Esc` key to exit.

**Example - Adding a New Filter:**

To add a new filter:

1. Create a new Python file (e.g., `my_filter.py`).
2. Define a class that inherits from `Filter` (from `template.py`).
3. Implement the `process()` method to perform your image processing.
4. Import and instantiate your filter in `main.py`, passing it the `Pipe` object.

This modular structure makes it easy to add, remove, or reorder filters in the video processing pipeline without modifying the core classes. 
