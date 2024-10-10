import cv2
import numpy as np


def detect_and_compute(image):
    sift = cv2.SIFT_create()

    keypoints, descriptors = sift.detectAndCompute(image, None)
    return keypoints, descriptors


def match_descriptors(des1, des2):
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    return good_matches


def stitch_images(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    kp1, des1 = detect_and_compute(gray1)
    kp2, des2 = detect_and_compute(gray2)

    matches = match_descriptors(des1, des2)

    # result_image = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=2)
    # cv2.imshow("matches", result_image)
    # cv2.waitKey(0)
    src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    # H, _ = cv2.findHomography(src_pts, dst_pts, cv2.LMEDS)

    height, width = img2.shape[:2]
    panorama = cv2.warpPerspective(img1, H, (width + img1.shape[1], height))

    panorama[0:height, 0:width] = img2
    cv2.imshow('img', panorama)
    cv2.waitKey(0)
    return panorama



def main() -> None:
    images = [cv2.imread('../images/campus/img1.jpg'),
              cv2.imread('../images/campus/img2.jpg'),
              cv2.imread('../images/campus/img3.jpg'),
              cv2.imread('../images/campus/img4.jpg')]


    panorama1 = stitch_images(images[3], images[2])
    panorama2 = stitch_images(panorama1, images[1])
    panorama3 = stitch_images(panorama2, images[0])

    cv2.imshow('panorama', panorama3)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
