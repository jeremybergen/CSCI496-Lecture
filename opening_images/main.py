import cv2
import numpy as np


def main() -> None:
    # img = cv2.imread("../images/OpenCV_Logo.jpg")

    img = cv2.imread("../images/tyu.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    # img_gray = img.copy()
    # img_gray = cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)

    # print(img[:5, 600:605])
    # img = 2*img
    # print(img[:5, 600:605])
    # # img = img.astype(np.uint8)
    # img = cv2.normalize(img, None, 0, 255, cv2.NORM_L2)
    # img = img.astype(np.uint8)
    # print(img[:5, 600:605])

    cv2.imshow("image", img)
    cv2.waitKey(0)

    # img_slice = img[img.shape[0]//2:img.shape[0]//2+100, :, :]
    # img[img.shape[0]//2-100:img.shape[0]//2] = img_slice
    #
    # cv2.imshow("image", img)
    # cv2.waitKey(0)
    # cv2.imshow("img_slice", img_slice)
    # cv2.waitKey(0)
    # img = cv2.cvtColor(img, cv2.COLOR_)

    # mean_img = np.mean(img, axis=2)
    # mean_img = mean_img.astype(np.uint8)
    # print(mean_img)
    # print(img.shape)

    # cv2.imshow("mean_img", mean_img)
    # cv2.waitKey(0)
    # print(mean_img)
    # print(img)

    # cv2.imshow("image", img)
    # cv2.waitKey(0)


if __name__ == '__main__':
    main()
