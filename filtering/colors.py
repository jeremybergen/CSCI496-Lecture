import cv2
import numpy as np


def createWindow() -> np.ndarray:
    img2 = cv2.imread("../images/PXL_20220814_151818246_small.jpg")
    return img2


img = createWindow()


def ontrackbarChanged(val) -> None:
    hue = cv2.getTrackbarPos("Hue", "HSVExample")
    hueHigh = cv2.getTrackbarPos("Hue High", "HSVExample")
    saturation = cv2.getTrackbarPos("Saturation", "HSVExample")
    saturationHigh = cv2.getTrackbarPos("Saturation High", "HSVExample")
    value = cv2.getTrackbarPos("Value", "HSVExample")
    valueHigh = cv2.getTrackbarPos("Value High", "HSVExample")

    # img = cv2.imread("../images/PXL_20220814_151818246_small.jpg")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    colorLow = np.array([hue, saturation, value])
    colorHigh = np.array([hueHigh, saturationHigh, valueHigh])

    mask = cv2.inRange(img2, colorLow, colorHigh)
    maskedImg = cv2.bitwise_and(gray_img, mask)

    # cv2.imshow("mask", mask)
    # cv2.imshow("maskedImg", maskedImg)
    # cv2.waitKey(0)
    # print(img[145:155, 45:55])
    # print(img2[145:155, 45:55])
    #
    # cv2.imshow("img", img)
    # cv2.imshow("img2", img2)
    # cv2.waitKey(0)

    cv2.imshow('HSVExample', maskedImg)
    return


def main() -> None:
    window = "HSVExample"

    cv2.namedWindow(window)

    cv2.createTrackbar("Hue", window, 0, 179, ontrackbarChanged)
    cv2.createTrackbar("Hue High", window, 0, 179, ontrackbarChanged)
    cv2.createTrackbar("Saturation", window, 0, 255, ontrackbarChanged)
    cv2.createTrackbar("Saturation High", window, 0, 255, ontrackbarChanged)
    cv2.createTrackbar("Value", window, 0, 255, ontrackbarChanged)
    cv2.createTrackbar("Value High", window, 0, 255, ontrackbarChanged)
    ontrackbarChanged(0)

    while True:
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break


if __name__ == '__main__':
    main()
