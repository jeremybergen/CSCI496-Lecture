import numpy as np
import cv2 as cv
# cap = cv.VideoCapture(cv.samples.findFile('../images/motion/PXL_20241024_011748179_small_cut.mp4'))
# cap = cv.VideoCapture(cv.samples.findFile('../images/motion/PXL_20241024_013723947_small.mp4'))
# cap = cv.VideoCapture('../images/motion/vtest.avi')
cap = cv.VideoCapture('../images/motion/slow_traffic_small.mp4')
ret, frame1 = cap.read()
prvs = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[..., 1] = 255
while(1):
    ret, frame2 = cap.read()
    if not ret:
        print('No frames grabbed!')
        break
    next = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
    flow = cv.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang*180/np.pi/2
    hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)
    bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    cv.imshow('frame2', bgr)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv.imwrite('opticalfb.png', frame2)
        cv.imwrite('opticalhsv.png', bgr)
        prvs = next
cv.destroyAllWindows()

# import numpy as np
# import cv2 as cv
# # import argparse
# # parser = argparse.ArgumentParser(description='This sample demonstrates Lucas-Kanade Optical Flow calculation. \
# #  The example file can be downloaded from: \
# #  https://www.bogotobogo.com/python/OpenCV_Python/images/mean_shift_tracking/slow_traffic_small.mp4')
# # parser.add_argument('image', type=str, help='path to image file')
# # args = parser.parse_args()
# # cap = cv.VideoCapture('../images/motion/PXL_20241024_011748179_small_cut.mp4')
# # cap = cv.VideoCapture('../images/motion/PXL_20241024_013723947_small.mp4')
# # cap = cv.VideoCapture('../images/motion/vtest.avi')
# cap = cv.VideoCapture('../images/motion/slow_traffic_small.mp4')
# # params for Shi-Tomasi corner detection
# feature_params = dict( maxCorners = 100,
#                        qualityLevel = 0.3,
#                        minDistance = 7,
#                        blockSize = 7 )
# # Parameters for lucas kanade optical flow
# lk_params = dict( winSize = (15, 15),
#                   maxLevel = 2,
#                   criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
# # Create some random colors
# color = np.random.randint(0, 255, (100, 3))
# # Take first frame and find corners in it
# ret, old_frame = cap.read()
# old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
# p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
# # Create a mask image for drawing purposes
# mask = np.zeros_like(old_frame)
# while 1:
#     ret, frame = cap.read()
#     if not ret:
#         print('No frames grabbed!')
#         break
#     frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # calculate optical flow
#     p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
#     # Select good points
#     if p1 is not None:
#         good_new = p1[st == 1]
#         good_old = p0[st == 1]
#         # draw the tracks
#         for i, (new, old) in enumerate(zip(good_new, good_old)):
#             a, b = new.ravel()
#             c, d = old.ravel()
#             mask = cv.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2)
#             frame = cv.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)
#             img = cv.add(frame, mask)
#         cv.imshow('frame', img)
#         k = cv.waitKey(30) & 0xff
#         if k == 27:
#             break
#         # Now update the previous frame and previous points
#         old_gray = frame_gray.copy()
#         p0 = good_new.reshape(-1, 1, 2)
# cv.destroyAllWindows()

# # import cv2
# # import numpy as np
# #
# # cap = cv2.VideoCapture('../images/motion/PXL_20241024_013723947_small.mp4')
# # # cap = cv2.VideoCapture('../images/motion/PXL_20241024_011748179_small.mp4')
# #
# # ret, frame1 = cap.read()
# # prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
# #
# # hsv = np.zeros_like(frame1)
# # hsv[..., 1] = 255
# #
# # while True:
# #     ret, frame2 = cap.read()
# #     if not ret:
# #         break
# #     next_frame = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
# #
# #     # Calculate dense optical flow
# #     flow = cv2.calcOpticalFlowFarneback(prvs, next_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)
# #
# #     # Convert flow to polar coordinates
# #     mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
# #     hsv[..., 0] = ang * 180 / np.pi / 2
# #     hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
# #
# #     # Convert HSV to RGB
# #     rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
# #
# #     cv2.imshow('Dense Optical Flow', rgb)
# #
# #     if cv2.waitKey(30) & 0xFF == 27:
# #         break
# #
# #     prvs = next_frame
# #
# # cap.release()
# # cv2.destroyAllWindows()
#
#
#
# import cv2
# import numpy as np
#
# # Load video or webcam
# # cap = cv2.VideoCapture('../images/motion/PXL_20241024_013723947_small.mp4')
# cap = cv2.VideoCapture('../images/motion/PXL_20241024_011748179_small_cut.mp4')
#
# # Parameters for Lucas-Kanade optical flow
# lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
#
# # Shi-Tomasi corner detection parameters
# feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)
#
# # Take the first frame and detect corners
# ret, old_frame = cap.read()
# old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
# p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
#
# # Create mask for drawing optical flow
# mask = np.zeros_like(old_frame)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # cv2.imshow('frame', frame_gray)
#     # cv2.waitKey(0)
#
#     # Calculate optical flow using Lucas-Kanade
#     p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
#
#     # Select good points
#     good_new = p1[st == 1]
#     good_old = p0[st == 1]
#
#     # Draw the tracks
#     for i, (new, old) in enumerate(zip(good_new, good_old)):
#         a, b = new.ravel()
#         c, d = old.ravel()
#         mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), (0, 255, 0), 2)
#         frame = cv2.circle(frame, (int(a), int(b) ), 5, (0, 0, 255), -1)
#
#     img = cv2.add(frame, mask)
#     cv2.imshow('Optical Flow', img)
#
#     if cv2.waitKey(30) & 0xFF == 27:
#         break
#
#     old_gray = frame_gray.copy()
#     p0 = good_new.reshape(-1, 1, 2)
#
# cap.release()
# cv2.destroyAllWindows()
