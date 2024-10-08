import cv2
import numpy as np


# def sign_axis(img: np.ndarray, sign=None) -> np.ndarray:
#     if sign == "yield":
#         #calculate angles for yield signs
#     elif sign == "warning":
#         #calculate angles for warning


def main():
    img = cv2.imread('green_diamond.png')
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    color_low = np.array([67, 200, 170])
    color_high = np.array([71, 220, 185])
    mask = cv2.inRange(img_hsv, color_low, color_high)
    edges = cv2.Canny(mask, 100, 200)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 15, 5, 0)
    if lines is not None:
        for line in lines:
            for x0, y0, x1, y1 in line:
                # print(np.arctan2(y1-y0, x1-x0)*180/np.pi)
                if 40 < np.abs(np.arctan2(y1-y0, x1-x0)*180/np.pi) < 50:
                    cv2.line(img, (x0, y0), (x1, y1), (0, 0, 255), 2)
    
    # print(lines)
    # cv2.imshow('edges', edges)
    # cv2.waitKey(0)
    # print(img_hsv[100, 100])
    cv2.imshow('img', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
