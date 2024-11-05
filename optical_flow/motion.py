import cv2
import numpy as np


def main() -> None:
    # cap = cv2.VideoCapture("../images/motion/slow_traffic_small.mp4")
    # cap = cv2.VideoCapture("../images/motion/PXL_20241024_013723947_small.mp4")
    cap = cv2.VideoCapture("../images/motion/PXL_20241024_011748179_small_cut.mp4")
    # cap = cv2.VideoCapture("../images/motion/vtest.avi")

    # ret, frame1 = cap.read()

    lk_params = dict( winSize = (15,15),
                      maxLevel = 2,
                      criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    step = 10

    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

    h, w = old_gray.shape
    p0 = np.array([[x, y] for y in range(0, h, step) for x in range(0, w, step)], dtype=np.float32).reshape(-1, 1, 2)



    while True:
        mask = np.zeros_like(old_frame)
        ret, frame = cap.read()
        if not ret:
            break

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

        if p1 is None or p0 is None:
            break

        good_new = p1[st == 1]
        good_old = p0[st == 1]

        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            a = int(a)
            b = int(b)
            c = int(c)
            d = int(d)
            frame = cv2.circle(frame, (a, b), 2, (0, 0, 255), -1)

        output = cv2.add(frame, mask)
        cv2.imshow('flow', output)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)

    cap.release()
    cv2.destroyAllWindows()


    # prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    # hsv = np.zeros_like(frame1)
    # hsv[..., 1] = 255
    # while True:
    #     ret, frame2 = cap.read()
    #     if not ret:
    #         break
    #     next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    #     flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    #
    #     mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    #     hsv[..., 0] = ang * 180 / np.pi / 2
    #     hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    #     bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    #     cv2.imshow('frame', bgr)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    # cap.release()
    # cv2.destroyAllWindows()

    # # Shi-Tomasi Corner Detection
    # feature_param = dict( maxCorners = 100,
    #                       qualityLevel = 0.3,
    #                       minDistance = 7,
    #                       blockSize = 7)
    #
    # lk_params = dict( winSize = (15,15),
    #                   maxLevel = 2,
    #                   criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    #
    # color = np.random.randint(0, 255, (100, 3))
    #
    # ret, old_frame = cap.read()
    #
    # old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    # p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_param)
    # mask = np.zeros_like(old_frame)
    #
    # while True:
    #     ret, frame = cap.read()
    #     if not ret:
    #         break
    #
    #     frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    #     if p1 is not None:
    #         good_new = p1[st == 1]
    #         good_old = p0[st == 1]
    #
    #         for i, (new, old) in enumerate(zip(good_new, good_old)):
    #             a, b = new.ravel()
    #             c, d = old.ravel()
    #             a = int(a)
    #             b = int(b)
    #             c = int(c)
    #             d = int(d)
    #             mask = cv2.line(mask, (a, b), (c, d), (0, 255, 0), 2)
    #             frame = cv2.circle(frame, (a, b), 5, (0, 0, 255), -1)
    #
    #         img = cv2.add(frame, mask)
    #         cv2.imshow('optical flow', img)
    #
    #         if cv2.waitKey(30) & 0xFF == 27:
    #             break
    #         old_gray = frame_gray.copy()
    #         p0 = good_new.reshape(-1, 1, 2)
    # cap.release()
    # cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
