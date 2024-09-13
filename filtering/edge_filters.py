import cv2
import numpy as np


def someFunction(img: np.ndarray, sign=None, sigma=0) -> None:
    pass

def main() -> None:
    img = cv2.imread('PXL_20230111_065654426_small.jpg', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('PXL_20230521_193353296_small.jpg', cv2.IMREAD_GRAYSCALE)

    # log_kernel = np.array([[0, -1, 0],
    #                        [-1, 4, -1],
    #                        [0, -1, 0]])

    log_kernel = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])

    log_img = cv2.filter2D(img, -1, log_kernel)
    shape = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    log_img_dilate = cv2.dilate(log_img, shape)
    log_img_erode = cv2.erode(log_img_dilate, shape)
    # cv2.imshow('log_img', log_img)
    # cv2.imshow('log_img_dilate', log_img_dilate)
    # cv2.imshow('log_img_erode', log_img_erode)
    # sobel_x = np.array([[-1, 0, 1],
    #                     [-2, 0, 2],
    #                     [-1, 0, 1]])

    # This is prewitt
    # sobel_x = np.array([[-1, 0, 1],
    #                     [-1, 0, 1],
    #                     [-1, 0, 1]])


    # sobel_y = sobel_x.T

    # sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, None, 3)
    # # sobel_x = cv2.normalize(sobel_x, None, 0, 255, cv2.NORM_MINMAX, 0)
    # sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, None, 3)
    # # sobel_y = cv2.normalize(sobel_y, None, 0, 255, cv2.NORM_MINMAX, 0)
    #
    # sobelx_img = cv2.filter2D(img, -1, sobel_x)
    # sobely_img = cv2.filter2D(img, -1, sobel_y)
    #
    # sobel_img = sobelx_img.astype(np.float64) + sobely_img.astype(np.float64)
    # sobel_img = cv2.normalize(sobel_img, None, 0, 255, cv2.NORM_MINMAX, 0)
    # ret, sobel_img = cv2.threshold(sobel_img, 127, 255, cv2.THRESH_BINARY)

    img_blur = cv2.GaussianBlur(img, (0, 0), 1.5)
    img_edge = cv2.Canny(img_blur, 100, 200)

    # cv2.imshow('sobelx', sobel_x)
    # cv2.imshow('sobely', sobel_y)
    # cv2.imshow('sobel', sobel_img)
    cv2.imshow('canny', img_edge)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
