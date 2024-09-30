## Real-time Video Processing Pipeline

#### Implementation based on *Pipes&Filters* architecture

This repository demonstrates a simple image processing pipeline using OpenCV in Python. The code showcases how to structure your project to apply a series of filters to a video stream from your webcam.

### Features:

- **Modular Design:**  The pipeline is designed using a modular approach, making it easy to add or remove image processing filters.
- **Pipe and Filter Pattern:**  The code utilizes a pipe and filter pattern for data flow. Each filter receives an image, processes it, and passes it along to the next filter in the pipeline.
- **Example Filters:** Includes example filters for:
    - **Red and Blue (RnB):** Removes the green channel from the image, creating a red and blue effect.
    - **Black and White (BnW):** Converts the image to grayscale.
    - **Mirror:** Flips the image horizontally.
    - **Resize:** Resizes the image to a specified width and height.
- **Window Display:**  Each stage of the pipeline can be displayed in separate OpenCV windows for visualization.

### Structure:

- **`template.py`:** Defines the core classes for the pipeline:
    - **`ImageData`:** Represents the image data flowing through the pipeline.
    - **`Pipe`:** Manages the flow of `ImageData` between filters.
    - **`Window`:**  Provides a way to display the image data in an OpenCV window.
    - **`Filter`:**  Abstract base class for image processing filters.
- **`main.py`:**  The main script that initializes the pipeline, reads the video stream, and applies the filters.
- **`filters/`:**  Contains the implementations of individual image processing filters.

### How to Run:

1. **Install OpenCV:**
   ```bash
   pip install opencv-python
   ```
2. **Run the main script:**
   ```bash
   python main.py
   ```

This will open multiple windows displaying the original video stream and the output after each filter is applied.

### Adding New Filters:

1. **Create a new Python file** in the `filters/` directory. 
2. **Define a class** that inherits from `Filter`.
3. **Implement the `process()` method** to apply your desired image processing logic.
4. **Import and instantiate** your new filter in `main.py` to add it to the pipeline.

### Future Improvements:

- Implement more advanced image processing filters.
- Introduce configuration options to enable/disable filters and adjust parameters.
- Explore parallel processing of filters for improved performance. 
