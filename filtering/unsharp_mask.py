import cv2
import numpy as np


def main() -> None:
    # img = cv2.imread('tyu.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('PXL_20220814_151818246_small.jpg', cv2.IMREAD_GRAYSCALE)

    blurred_img = cv2.GaussianBlur(img, (5, 5), 1)
    # print(blurred_img[10:20, 10:20])
    # print(f"img[11:12, 11:12]: {img[12:13, 12:13]}, blurred_img[11:12, 11:12]: {blurred_img[12:13, 12:13]}")

    # mask = img.astype(np.float64) - blurred_img.astype(np.float64)
    mask = cv2.subtract(img, blurred_img)
    # print(mask[10:20, 10:20])

    scale_val = 1.5

    unsharp_img = img.astype(np.float64) + (mask * scale_val)

    unsharp_img = cv2.normalize(unsharp_img, unsharp_img, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    cv2.imshow('image', img)
    cv2.imshow('unsharp_img', unsharp_img)
    cv2.waitKey(0)





    # sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    # sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    #
    # blur_img = cv2.GaussianBlur(img, (5, 5), .5)
    #
    # grad_x = cv2.filter2D(blur_img, -1, sobel_x)
    # grad_y = cv2.filter2D(blur_img, -1, sobel_y)
    #
    # ret, grad_x = cv2.threshold(grad_x, 127, 255, cv2.THRESH_BINARY)
    # ret, grad_y = cv2.threshold(grad_y, 127, 255, cv2.THRESH_BINARY)
    #
    # comb_filter = grad_x + grad_y
    #
    # cv2.imshow('image', img)
    # cv2.imshow('grad_x', grad_x)
    # cv2.imshow('grad_y', grad_y)
    # cv2.imshow('combined', comb_filter)
    # cv2.waitKey(0)

    # blurred_img = cv2.GaussianBlur(img, (5, 5), 2.5)
    # # # cv2.imshow('blurred', blurred_img)
    # #
    # # # mask = img.astype(np.float64) - blurred_img.astype(np.float64)
    # mask = img - blurred_img
    # # # cv2.imshow('mask', mask)
    # # mask = cv2.subtract(img, blurred_img)
    # # print(mask)
    # # cv2.imshow('mask', mask)
    # #
    # scale_val = 1.5
    # #
    # # sharpened_img = img.astype(np.float64) + scale_val * mask.astype(np.float64)
    # # cv2.normalize(sharpened_img, sharpened_img, 0, 255, cv2.NORM_MINMAX)
    # # sharpened_img = sharpened_img.astype(np.uint8)
    # # # print(sharpened_img.astype(np.uint8))
    #
    # sharpened_img = cv2.addWeighted(img, 1.0 + scale_val, blurred_img, -scale_val, 0)
    #
    # sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    # sharpened_img2 = cv2.filter2D(img, -1, sharpen_kernel)
    #
    # # cv2.imshow('sharpened image2', sharpened_img2)
    # cv2.imshow('original', img)
    # cv2.imshow('sharpened image', sharpened_img)
    # cv2.waitKey(0)


if __name__ == '__main__':
    main()
