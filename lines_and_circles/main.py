import cv2
import numpy as np


def main() -> None:
    img = cv2.imread('coins.jpg')
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print(img_hsv[10:20, 10:20])
    color_low = np.array([13, 20, 250])
    color_high = np.array([30, 100, 255])
    img_mask = cv2.inRange(img_hsv, color_low, color_high)
    cv2.imshow('img_mask', img_mask)
    cv2.waitKey(0)
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img_blur = cv2.GaussianBlur(img_gray, (0, 0), 1.5)
    # img_edge = cv2.Canny(img_blur, 50, 150)
    #
    # # circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, 10, None, 200, 100, 0, 0)
    # circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, 1, param1=150, param2=50, minRadius=1, maxRadius=0)
    #
    # print(circles)
    # if circles is not None:
    #     for circle in circles[0]:
    #         x, y, radius = circle
    #         x = int(x)
    #         y = int(y)
    #         cv2.circle(img, (x, y), int(radius), (0, 0, 255), 2)
    # img = cv2.imread('../filtering/PXL_20230414_025654297_small.jpg')
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img_blur = cv2.GaussianBlur(img_gray, (0, 0), 1.5)
    # img_edge = cv2.Canny(img_blur, 100, 200)
    #
    # lines = cv2.HoughLinesP(img_edge, 1, np.pi / 180, 50, None, 5, 5)
    # print(lines)
    # if lines is not None:
    #     for line in lines:
    #         x0, y0, x1, y1 = line[0]
    #         cv2.line(img, (x0, y0), (x1, y1), (0, 0, 255), 2, cv2.LINE_AA)
    # lines = cv2.HoughLines(img_edge, 1, np.pi / 180, 100)
    # # print(lines)
    # if lines is not None:
    #     for i in range(0, len(lines)):
    #         rho = lines[i][0][0]
    #         theta = lines[i][0][1]
    #         a = np.cos(theta)
    #         b = np.sin(theta)
    #         x0 = a * rho
    #         y0 = b * rho
    #         pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
    #         pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
    #         cv2.line(img, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

    # cv2.imshow('edge', img_edge)
    # # # cv2.waitKey(0)
    # cv2.imshow('img', img)
    cv2.imshow('img_hsv', img_hsv)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()