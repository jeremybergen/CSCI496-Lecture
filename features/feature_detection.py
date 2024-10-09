import cv2
import numpy as np


def detect_and_compute(image):
    sift = cv2.SIFT_create()

    keypoints, descriptors = sift.detectAndCompute(image, None)
    return keypoints, descriptors


def main() -> None:
    image1 = cv2.imread("../images/office/board.jpg")
    image2 = cv2.imread("../images/office/board_scene.jpg")
    gray_img1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    kp1, des1 = detect_and_compute(gray_img1)
    kp2, des2 = detect_and_compute(gray_img2)

    # out_img = cv2.drawKeypoints(gray_img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # out_img1 = cv2.drawKeypoints(gray_img1, kp1, None, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # out_img2 = cv2.drawKeypoints(gray_img2, kp2, None, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.65 * n.distance:
            good_matches.append(m)

    result_image = cv2.drawMatches(image1, kp1, image2, kp2, good_matches, None, flags=2)
    cv2.imshow("matches", result_image)

    # cv2.imshow("SIFT", out_img1)
    # cv2.imshow("SIFT2", out_img2)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
