import cv2
import numpy as np
import time
import mediapipe as mp
from src.drawtext import *
from src.drawdict import drawLandmarks


def main():
    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic

    cap = cv2.VideoCapture(0)
    nativeFPS = cap.get(cv2.CAP_PROP_FPS)

    ## Setup mediapipe instance
    with mp_holistic.Holistic(
        min_detection_confidence=0.5, min_tracking_confidence=0.5
    ) as holistic:

        while cap.isOpened():
            success, frame = cap.read()
            start = time.time()

            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = holistic.process(image)

            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Draw landmarks
            drawLandmarks(image, results, mp_holistic, mp_drawing)

            # Draw text
            text = getFpsText(start, nativeFPS)
            putTextTemplate(cv2, image, text)

            # Render frame
            cv2.imshow("MediaPipe Feed", image)

            # Escape key 'q' to quit
            if cv2.waitKey(5) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
