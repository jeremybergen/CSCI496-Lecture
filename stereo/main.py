import cv2
import numpy as np


def main() -> None:
    img_left = cv2.imread('view1_small.png')
    img_left_gray = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
    img_right = cv2.imread('view5_small.png')
    img_right_gray = cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY)

    stereo = cv2.StereoSGBM_create(minDisparity=1, numDisparities=64, blockSize=1,
                                   speckleWindowSize=200, speckleRange=4)

    disp = stereo.compute(img_left_gray, img_right_gray).astype(np.float64)
    disp_right = stereo.compute(img_right_gray, img_left_gray).astype(np.float64)
    disp = cv2.normalize(disp, 0, 255, cv2.NORM_MINMAX)
    disp_right = cv2.normalize(disp_right, 0, 255, cv2.NORM_MINMAX)

    wls = cv2.ximgproc.createDisparityWLSFilter(stereo)
    filtered_disparity_map = wls.filter(disp, img_left_gray, disparity_map_right=disp_right)

    cv2.imshow("Disparity", disp)
    cv2.imshow("Disparity right", disp_right)
    cv2.imshow("filtered disparity", filtered_disparity_map)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
