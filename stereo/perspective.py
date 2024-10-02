import cv2
import numpy as np


def main():
    img = cv2.imread('NFL_header.jpg.webp')
    pts1 = np.float32([[565, 0], [1493, 0], [239, 1079], [1819, 1079]])
    pts2 = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])

    M = cv2.getPerspectiveTransform(pts1, pts2)
    # print(M)
    dst = cv2.warpPerspective(img, M, (500, 500))
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.imshow('dst', dst)
    cv2.waitKey(0)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)


if __name__ == "__main__":
    main()