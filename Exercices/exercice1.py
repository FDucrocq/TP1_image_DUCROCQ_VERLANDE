import cv2.cv2 as cv
import numpy as np

# CONFIGURATION
threshold = 40


def save_webcam(outPath, fps, mirror=False):
    # Capturing video from webcam:
    cap = cv.VideoCapture(0)
    currentFrame = 0
    # Get current width of frame
    width = cap.get(cv.CAP_PROP_FRAME_WIDTH)  # float
    # Get current height of frame
    height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)  # float
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*"XVID")
    out = cv.VideoWriter(outPath, fourcc, fps, (int(width), int(height)))

    prev_ret, prev_frame = cap.read()
    if prev_ret:
        prev_frame = cv.flip(prev_frame, 1)

    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            if mirror:
                # Mirror the output video frame
                frame = cv.flip(frame, 1)
            # Saves for video
            out.write(frame)

            # Calculate the distance of the 2 pictures
            diff = np.sum((prev_frame.astype("float") - frame.astype("float")) * (prev_frame.astype("float") - frame.astype("float")) )
            diff = diff/(prev_frame.shape[0] * frame.shape[1])

            if diff > threshold:
                print("/!\ Attention /!\ Quelqu'un s'est introduit dans la matrice !" + diff.__str__())

            prev_frame = frame

            # Display the resulting frame
            cv.imshow('frame', frame)
        else:
            break

        if cv.waitKey(1) & 0xFF == ord('q'):  # if 'q' is pressed then quit
            break

        # To stop duplicate images
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    out.release()
    cv.destroyAllWindows()


def main():
    save_webcam('output.avi', 30.0, mirror=True)


if __name__ == '__main__':
    main()