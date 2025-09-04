import cv2
import numpy as np


def main() -> None:
    # img = cv2.imread("../images/tyu.jpg", cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread("../images/PXL_20220814_151818246_small.jpg", cv2.IMREAD_GRAYSCALE)
    img = cv2.imread("../images/PXL_20211006_195833767_small.jpg", cv2.IMREAD_GRAYSCALE)
    img2 = img.copy()

    # imgFilter = np.ones((101, 101)).astype(np.float64)
    # imgFilter = 1/np.sum(imgFilter, axis=None) * imgFilter
    # imgFilter2 = np.array(
    #     [[1, 2, 1],
    #      [2, 4, 2],
    #      [1, 2, 1]]
    # )
    # imgFilter2 = 1/np.sum(imgFilter2, axis=None) * imgFilter2
    # print(imgFilter2)
    # # quit()
    # cv2.filter2D(img, -1, imgFilter, img2, borderType=cv2.BORDER_REPLICATE)

    # print(imgFilter)

    # imgKernel = cv2.getGaussianKernel(3, 0)
    # print(imgKernel)
    # quit()

    # img2 = cv2.GaussianBlur(img, (11, 11), 100)

    # cv2.imshow("img", img)
    # kernel = np.array([[0, 0, 0], [0, 2, 0], [0, 0, 0]])
    # kernel = np.array([[0, 0, 0], [0, 2, 0], [0, 0, 0]]) - 1/18 * np.array([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
    # img2 = cv2.filter2D(img2, -1, kernel)

    # blurredImg = cv2.GaussianBlur(img, (5, 5), 1.0)
    # cv2.imshow("blurredImg", blurredImg)
    #
    # # mask = img.astype(np.float64) - blurredImg.astype(np.float64)
    # # print(mask[174,189])
    # # cv2.normalize(mask, mask, 0, 255, cv2.NORM_MINMAX)
    # # mask = mask.astype(np.uint8)
    # mask = cv2.subtract(img, blurredImg)
    # cv2.imshow("mask", mask)
    #
    # scaledMask = mask.astype(np.float64) * 1.5
    # cv2.normalize(scaledMask, scaledMask, 0, 255, cv2.NORM_MINMAX)
    # scaledMask = scaledMask.astype(np.uint8)
    # cv2.imshow("scaledMask", scaledMask)
    #
    # # sharpened = img.astype(np.float64) - scaledMask.astype(np.float64)
    # # cv2.normalize(sharpened, sharpened, 0, 255, cv2.NORM_MINMAX)
    # # sharpened = sharpened.astype(np.uint8)
    # sharpened = img.astype(np.float64) + scaledMask.astype(np.float64)
    # cv2.normalize(sharpened, sharpened, 0, 255, cv2.NORM_MINMAX)
    # sharpened = sharpened.astype(np.uint8)
    # cv2.imshow("sharpened", sharpened)

    # unsharpKernel = ([[0, 0, 0],
    #                  [0, 1, 0],
    #                  [0, 0, 0]]
    #               + ([[0, 0, 0],
    #                   [0, 1, 0],
    #                   [0, 0, 0]]
    #       - np.array([[0, 1, 0],
    #                   [1, 1, 1],
    #                   [0, 1, 0]])/5) * 5)
    # unsharpKernel2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    # sharpImg = cv2.filter2D(img, -1, unsharpKernel)
    # sharpImg2 = cv2.filter2D(img, -1, unsharpKernel2)
    # # kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    # # img2 = cv2.filter2D(img, -1, kernel)
    # # kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])/5
    # # img3 = cv2.filter2D(img, -1, kernel)
    # #
    # # sharpImg = img2 + cv2.subtract(img2, img3) * 5
    #
    # cv2.imshow("sharpImg", sharpImg)
    # cv2.imshow("sharpImg2", sharpImg2)

    kernel = np.array([[-10, 0, 10],
                       [-50, 0, 50],
                       [-10, 0, 10]])
    kernel = 1/8 * kernel

    kernely = np.array([[3, 10, 3],
                        [0, 0, 0],
                        [-3, -10, -3]])
    kernely = 1/8 * kernely
    # np.array([[-1, -1, -1],
    #           [0, 0, 0],
    #           [1, 1, 1]])
    # img = cv2.GaussianBlur(img, (5, 5), 2.5)
    sobelx = cv2.filter2D(img, -1, kernel)
    sobely = cv2.filter2D(img, -1, kernely)
    # kernel = kernel.T
    # sobely = cv2.filter2D(img, -1, kernel)

    # combImg = sobelx.astype(np.float64) + sobely.astype(np.float64)

    # cv2.normalize(combImg, combImg, 0, 255, cv2.NORM_MINMAX)
    # combImg = combImg.astype(np.uint8)
    # ret, combImg = cv2.threshold(combImg, 90, 255, cv2.THRESH_BINARY)
    # sobelx = cv2.Sobel(img, -1, 1, 1, ksize=3)
    # sobelx = cv2.Scharr(img, -1, .5, .5)
    cv2.imshow("sobelx", sobelx)
    # cv2.imshow("sobely", sobely)
    # cv2.imshow("combImg", combImg)
    cv2.imshow("img", img)
    # cv2.imshow("img2", img2)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()

