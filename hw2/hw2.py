import cv2
import numpy as np


# def sign_axis(img: np.ndarray, sign=None) -> np.ndarray:
#     if sign == "yield":
#         #calculate angles for yield signs
#     elif sign == "warning":
#         #calculate angles for warning


def main():
    img = cv2.imread('green_diamond.png')
    # img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # color_low = np.array([67, 200, 170])
    # color_high = np.array([71, 220, 185])
    # mask = cv2.inRange(img_hsv, color_low, color_high)
    # edges = cv2.Canny(mask, 100, 200)
    # lines = cv2.HoughLinesP(edges, 1, np.pi/180, 15, 5, 0)
    # if lines is not None:
    #     for line in lines:
    #         for x0, y0, x1, y1 in line:
    #             # print(np.arctan2(y1-y0, x1-x0)*180/np.pi)
    #             if 40 < np.abs(np.arctan2(y1-y0, x1-x0)*180/np.pi) < 50:
    #                 cv2.line(img, (x0, y0), (x1, y1), (0, 0, 255), 2)
    noisy_image = np.copy(img).astype(np.float64)
    # cv2.imshow('img', img)
    # cv2.imshow('noisy_img', noisy_image)
    # cv2.waitKey(0)
    mean = np.mean(img)
    sigma = 25
    gaussian = np.random.normal(mean, sigma, (img.shape[0],img.shape[1]))
    # print(gaussian)
    noisy_image[:, :, 0] = img[:, :, 0] + gaussian
    noisy_image[:, :, 1] = img[:, :, 1] + gaussian
    noisy_image[:, :, 2] = img[:, :, 2] + gaussian
    noisy_image = cv2.normalize(noisy_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    noisy_image = cv2.GaussianBlur(noisy_image, (0, 0), 1.5)
    noisy_image = cv2.cvtColor(noisy_image, cv2.COLOR_BGR2HSV)
    print(noisy_image[95:105, 95:105])
    color_low = np.array([65, 100, 120])
    color_high = np.array([75, 150, 170])
    mask = cv2.inRange(noisy_image, color_low, color_high)
    cv2.imshow('non-dilated mask', mask)

    element = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * 3 + 1, 2 * 3 + 1),
                                       (3, 3))
    mask = cv2.dilate(mask, element)
    cv2.imshow('dilated mask', mask)
    cv2.waitKey(0)
    # print(lines)
    # cv2.imshow('edges', edges)
    # cv2.waitKey(0)
    # print(img_hsv[100, 100])
    cv2.imshow('img', noisy_image)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()
