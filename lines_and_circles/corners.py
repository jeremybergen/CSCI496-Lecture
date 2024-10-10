import cv2
import numpy as np


def main() -> None:
    # img = cv2.imread('../filtering/PXL_20211006_195833767_small.jpg')
    img = cv2.imread('../filtering/PXL_20220814_151818246_small.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)

    corners = cv2.cornerHarris(src=gray, blockSize=2, ksize=3, k=0.04)

    corner_response = cv2.dilate(corners, None)

    threshold = 0.01 * corner_response.max()
    img[corner_response > threshold] = [0, 0, 255]

    cv2.imshow('img', img)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
