import cv2
import numpy as np


def main() -> None:
    img = cv2.imread('PXL_20211006_195833767_small.jpg')
    # translation_matrix = np.array([[1.5*1, 0, 50],
    #                                [0, 1.5*1, 150]]).astype(np.float64)
    # translation_matrix = np.array([[0, 1, 377],
    #                                [-1, 0, 0]]).astype(np.float64)

    translation_matrix = np.array([[.5*np.cos(45*np.pi/180), .5*-np.sin(45*np.pi/180), 0],
                                   [.5*np.sin(45*np.pi/180), .5*np.cos(45*np.pi/180), 0]]).astype(np.float64)
    translation_matrix[:2, 2] = np.array(img.shape[:2][::-1])//2 - np.matmul(translation_matrix[:2, :2], np.array(img.shape[:2][::-1])//2)
    print(f"img.shape[:2][::-1]: {img.shape[:2][::-1]}")
    print(f"np.matmul(translation_matrix[:2, :2], np.array(img.shape[:2][::-1])//2: {np.matmul(translation_matrix[:2, :2], np.array(img.shape[:2][::-1])//2)}")
    print(f"translation_matrix[:2, :2]@np.array(img.shape[:2][::-1])//2: {translation_matrix[:2, :2]@np.array(img.shape[:2][::-1])//2}")
    print(f"translation_matrix: {translation_matrix}")
    
    translated_img = cv2.warpAffine(img, translation_matrix, (img.shape[1], img.shape[0]))
    cv2.imshow('img', img)
    cv2.imshow('translated_img', translated_img)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
