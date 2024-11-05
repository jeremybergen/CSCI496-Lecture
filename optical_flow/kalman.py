import cv2
import numpy as np


def main() -> None:
    cap = cv2.VideoCapture("../images/motion/output.mp4")
    kf = cv2.KalmanFilter(4, 2)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # print(frame[180, 470])
        # print(frame[470, 180])
        color_low = np.array([7, 150, 100])
        color_high = np.array([15, 200, 155])
        mask = cv2.inRange(frame, color_low, color_high)

        edges = cv2.Canny(mask, 100, 200)
        x, y, w, h = cv2.boundingRect(edges)

        cent_x = x + w//2
        cent_y = y + h//2

        pred = kf.predict()
        measurement = np.array([[cent_x], [cent_y]], np.float32)
        kf.correct(measurement)

        cv2.circle(frame, (int(pred[0]), int(pred[1])), 3, (0, 255, 0), 2)
        cv2.circle(frame, (cent_x, cent_y), 3, (255, 0, 0), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()
