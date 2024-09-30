import cv2
from template import Pipe, ImageData
from BnW import BnWFilter
from mirror import MirrorFilter
from resize import ResizeFilter
from RnB import RnBFilter

if __name__ == "__main__":
    video_source = 0  # 0 for webcam, or path to video file

    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    pipe = Pipe()

    # Create filters (RnB before BnW to get correct colors)
    rnb_filter = RnBFilter(pipe)
    grayscale_filter = BnWFilter(pipe)
    mirror_filter = MirrorFilter(pipe)
    resize_filter = ResizeFilter(pipe)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        pipe.put(ImageData(frame, frame))  # Put ImageData into pipeline
        
        # Filter processing
        rnb_filter.process()
        grayscale_filter.process()
        mirror_filter.process()
        resize_filter.process()

        final_data = pipe.get()  # Get ImageData from last pipe
        final_frame = final_data.cur_image 

        cv2.imshow('Processed Video', final_frame)

        c = cv2.waitKey(1)
        if c == 27:  # Press Esc to exit
            break

    cap.release()
    cv2.destroyAllWindows()