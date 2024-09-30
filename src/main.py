import cv2
from template import Pipe, ImageData, Window
from filters.BnW import BnWFilter
from filters.mirror import MirrorFilter
from filters.resize import ResizeFilter
from filters.RnB import RnBFilter


if __name__ == "__main__":
    video_source = 0  # 0 for webcam, or path to video file

    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    pipe = Pipe()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        pipe.put(ImageData(frame))  # Put ImageData into pipeline

        # --- Section of pipes and filters ---

        Window(1).show(pipe)

        # Create and process the filters
        RnBFilter(pipe).process()

        Window(2).show(pipe)

        # Create and process the filters
        MirrorFilter(pipe).process()

        Window('test').show(pipe)

        # Create and process the filters
        BnWFilter(pipe).process()
        RnBFilter(pipe).process()
        ResizeFilter(pipe, 500, 500).process()

        Window(3).show(pipe)

        # --- End of section ---

        c = cv2.waitKey(1)
        if c == 27:  # Press Esc to exit
            break

    cap.release()
    cv2.destroyAllWindows()
