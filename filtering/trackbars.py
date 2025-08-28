import cv2
import numpy as np


def createWindow() -> np.ndarray:
    img2 = cv2.imread("../images/PXL_20220814_151818246_small.jpg")
    return img2


img = createWindow()


def ontrackbarChanged(val) -> None:
    sigma = cv2.getTrackbarPos('sigma', 'BlurExample')
    ksize = cv2.getTrackbarPos('ksize', 'BlurExample')
    if ksize%2 == 0:
        ksize = ksize - 1
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if sigma == 0 or ksize == 0:
        return
    blur_img = cv2.GaussianBlur(gray_img, (ksize, ksize), sigma, borderType=cv2.BORDER_CONSTANT)
    cv2.imshow('BlurExample', blur_img)
    return


def main() -> None:
    window = "BlurExample"

    cv2.namedWindow(window)

    cv2.createTrackbar("sigma", window, 1, 40, ontrackbarChanged)
    cv2.createTrackbar("ksize", window, 1, 100, ontrackbarChanged)
    ontrackbarChanged(0)

    while True:
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break


if __name__ == '__main__':
    main()
