import cv2
import numpy as np
import matplotlib.pyplot as plt


def create_window() -> np.ndarray:
    img2 = cv2.imread('tyu.jpg')
    return img2


img = create_window()


def ontrackbar_changed(val) -> None:
    sigma = cv2.getTrackbarPos("sigma", "BlurExample")
    threshold = cv2.getTrackbarPos("threshold", "BlurExample")
    # gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # gray_img = img[:, :, 2]
    # binary_img = np.zeros_like(img)
    # for i in gray_img:
    #     for j in gray_img[i]:
    #         print(gray_img[i][j])
            # if gray_img[i, j] > 127:
            #     binary_img[i, j] = 255

    ret, binary_img = cv2.threshold(gray_img, threshold, 255, cv2.THRESH_BINARY)


    if sigma == 0:
        return
    blur_img = cv2.GaussianBlur(gray_img, (0, 0), sigma)
    cv2.imshow("BlurExample", blur_img)
    return


def main() -> None:
    window = "BlurExample"

    cv2.namedWindow(window)

    cv2.createTrackbar("sigma", window, 1, 40, ontrackbar_changed)
    cv2.createTrackbar("threshold", window, 1, 255, ontrackbar_changed)

    ontrackbar_changed(0)

    while True:
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    # linear_kernel = np.ones((3, 3), np.float64) / 9
    # gaussian_kernel = np.array([
    #     [1, 2, 1],
    #     [2, 4, 2],
    #     [1, 2, 1]
    # ], dtype=np.float64)/16

    # gaussian_kernel = cv2.getGaussianKernel(3, 3)
    # print(gaussian_kernel)
    # blurred_image = cv2.filter2D(img, -1, gaussian_kernel)
    # blurred_image = cv2.GaussianBlur(img, (3, 3), 1.5)
    #
    # cv2.imshow(window, img)
    # cv2.imshow(window+"2", blurred_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    pass


if __name__ == '__main__':
    main()
