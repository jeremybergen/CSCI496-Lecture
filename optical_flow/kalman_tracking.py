import cv2
import numpy as np


# kf = cv2.KalmanFilter(4, 2)  # 4 state variables (x, y, dx, dy), 2 measurements (x, y)
# kf.transitionMatrix = np.array([[1, 0, 1, 0],
#                                 [0, 1, 0, 1],
#                                 [0, 0, 1, 0],
#                                 [0, 0, 0, 1]], np.float32)
#
# kf.measurementMatrix = np.array([[1, 0, 0, 0],
#                                  [0, 1, 0, 0]], np.float32)
# kf.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03
# kf.measurementNoiseCov = np.eye(2, dtype=np.float32) * 0.5
# kf.statePost = np.array([[0], [0], [0], [0]], np.float32)
#
# # Dummy data (or connect to a video feed)
# measurements = np.array([[i + np.random.randn()*0.5,
#                           j + np.random.randn()*0.5] for i, j in zip(range(0, 100, 5), range(0, 100, 5))], np.float32)
#
# # Tracking loop
# for measurement in measurements:
#     pred = kf.predict()
#     kf.correct(measurement)
#     print("Predicted:", pred.ravel(), "Measured:", measurement)

cap = cv2.VideoCapture("output.mp4")
kf = cv2.KalmanFilter(4, 2)
# (initialize matrices as in previous code)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detect object position (simple threshold example)
    # Assume we get `x, y` position
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    print(frame[173, 391])
    # print(frame[470, 180])
    color_low = np.array([7, 150, 100])
    color_high = np.array([15, 200, 255])
    mask = cv2.inRange(frame, color_low, color_high)
    cv2.imshow('mask', frame)
    cv2.waitKey(1)
    # dilatation_size = 500
    # dilation_shape = cv2.MORPH_RECT
    # element = cv2.getStructuringElement(dilation_shape, (2 * dilatation_size + 1, 2 * dilatation_size + 1),
    #                                    (dilatation_size, dilatation_size))
    # dilatation_dst = cv2.dilate(mask, element)

    # contours, hier = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # print(contours)
    # for cnt in contours:
    #     if 200 < cv2.contourArea(cnt) < 5000:
    #         cv2.drawContours(frame, [cnt], 0, (0, 255, 0), 2)
    #         cv2.drawContours(mask, [cnt], 0, 255, -1)
    edges = cv2.Canny(mask, 100, 200)
    x, y, w, h = cv2.boundingRect(edges)
    # print(x_min, y_min, x_max, y_max)
    # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #
    # cv2.imshow('frame', frame)
    # cv2.waitKey(0)

    cent_x = x+w//2
    cent_y = y+h//2

    pred = kf.predict()
    measurement = np.array([[cent_x], [cent_y]], np.float32)
    kf.correct(measurement)

    # Draw predicted and measured positions
    cv2.circle(frame, (int(pred[0]), int(pred[1])), 3, (0, 255, 0), -1)
    cv2.circle(frame, (cent_x, cent_y), 3, (255, 0, 0), -1)
    # cv2.imshow("Tracking", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
