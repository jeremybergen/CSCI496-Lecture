import cv2
import numpy as np


def main() -> None:
    img = cv2.imread("../images/tyu.jpg", cv2.IMREAD_GRAYSCALE)
    img2 = img.copy()

    # imgFilter = np.ones((101, 101)).astype(np.float64)
    # imgFilter = 1/np.sum(imgFilter, axis=None) * imgFilter
    imgFilter2 = np.array(
        [[1, 2, 1],
         [2, 4, 2],
         [1, 2, 1]]
    )
    imgFilter2 = 1/np.sum(imgFilter2, axis=None) * imgFilter2
    print(imgFilter2)
    # # quit()
    # cv2.filter2D(img, -1, imgFilter, img2, borderType=cv2.BORDER_REPLICATE)

    # print(imgFilter)

    imgKernel = cv2.getGaussianKernel(3, 0)
    print(imgKernel)
    quit()

    img2 = cv2.GaussianBlur(img, (11, 11), 25)

    cv2.imshow("img", img)
    cv2.imshow("img2", img2)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()

